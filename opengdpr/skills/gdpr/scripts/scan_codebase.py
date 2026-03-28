#!/usr/bin/env python3
"""
GDPR Compliance Scanner v0.5.0
Creativa Legal — https://creativa.legal
License: GPL-3.0

Determinististic regex-based scanner for GDPR compliance issues in source code.
Outputs JSON to stdout. No external dependencies (stdlib only).

Usage:
    python scan_codebase.py /path/to/project [--module sub/path]
"""

import re
import os
import sys
import json
import hashlib
import time
from pathlib import Path
from datetime import datetime, timezone

# ─── Configuration ────────────────────────────────────────────────────────────

SCANNER_VERSION = "0.5.0"

SKIP_DIRS = {
    "node_modules", ".git", "vendor", "build", "dist", "__pycache__",
    ".venv", "venv", ".next", ".nuxt", "target", "bin", "obj", ".cache",
    ".tox", ".eggs", "*.egg-info", ".mypy_cache", ".pytest_cache",
    "coverage", ".nyc_output", "out", "public/static", "static/dist",
}

SCAN_EXTENSIONS = {
    ".js", ".ts", ".jsx", ".tsx", ".py", ".java", ".kt", ".go", ".rb",
    ".php", ".cs", ".swift", ".dart", ".rs", ".vue", ".svelte", ".html",
    ".yml", ".yaml", ".json", ".env", ".cfg", ".ini", ".toml", ".xml",
    ".sql", ".mod", ".graphql", ".gql",
}

# Config files that generate too many false positives from metadata
SKIP_CONFIG_FILES = {
    "package.json", "package-lock.json", "yarn.lock", "pnpm-lock.yaml",
    "tsconfig.json", "tsconfig.base.json", "jsconfig.json",
    "turbo.json", "biome.json", "eslint.json", ".eslintrc.json",
    "prettier.json", ".prettierrc.json", "babel.config.json",
    "jest.config.json", "vitest.config.json", "webpack.config.json",
    "rollup.config.json", "vite.config.json", "next.config.json",
    "nuxt.config.json", "svelte.config.json", "astro.config.json",
}

# Test file markers
TEST_FILE_MARKERS = {".test.js", ".spec.js", ".test.ts", ".spec.ts", "__tests__"}

# Locale file markers (i18n)
I18N_FILE_MARKERS = {"i18n", "locales", "translations", "lang", "locale"}

# Config/spec/test file pattern detection (SH2)
CONFIG_SPEC_TEST_PATTERNS = {
    "config", "spec", "test", "fixture", "mock", "setup", "example",
    "demo", "sample", "stub", ".example.", ".sample.",
}

# Extended TEST_VALUES (SH1)
TEST_VALUES = {
    "test@example.com", "user@test.com", "admin@test.com", "fake@test.com",
    "dummy@test.com", "qa@test.com", "staging@test.com", "dev@test.com",
    "example@example.com", "sample@example.com", "test.user@example.com",
    "4111111111111111", "5555555555554444", "378282246310005", "6011111111111117",
    "3530111333300000", "3566002020360505", "4532015112830366", "6011000990139424",
    "DE89370400440532013000", "GB82WEST12345698765432", "FR1420041010050500013M02606",
    "IT60X0542811101000000123456", "ES9121000418450200051332", "NL91ABNA0417164300",
    "AT611904300234573201", "CH9300762011623852957", "CZ6508000000192000145399",
    "DK5000400440116243", "BE68539007547034", "LU280019400644750000",
    "PT50002700001100023600174", "SE4550000000058398257466", "SK3112000000198742637541",
    "test", "foo", "bar", "baz", "example", "demo", "sample", "fixture",
}

# Extended analytics/consent libraries (SH6)
ANALYTICS_CONSENT_LIBRARIES = {
    "cookiebot", "onetrust", "didomi", "klaro", "tarteaucitron", "osano",
    "cookiehub", "axeptio", "iubenda", "quantcast", "civic_cookie_control",
}

# ─── GDPR Patterns ────────────────────────────────────────────────────────────

PATTERNS = {
    # PII & Personal Data Detection
    "email": {
        "pattern": r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}",
        "severity": "MEDIUM",
        "article": "Art. 4, 6",
        "description": "Email address detected",
        "guidance": "Ensure email processing has valid legal basis (Art. 6) and required notices (Art. 14)"
    },
    "credit_card": {
        "pattern": r"\b(?:\d{4}[-\s]?){3}\d{4}\b|\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|6(?:011|5[0-9]{2})[0-9]{12}|(?:2131|1800|35\d{3})\d{11})\b",
        "severity": "CRITICAL",
        "article": "Art. 4, 6, 32",
        "description": "Credit card number detected",
        "guidance": "Payment data should only be transmitted via PCI-DSS compliant systems (Art. 32)"
    },
    "ssn": {
        "pattern": r"\b(?:\d{3}-\d{2}-\d{4}|\d{3}\.\d{2}\.\d{4}|\d{9})\b",
        "severity": "CRITICAL",
        "article": "Art. 4, 6, 32",
        "description": "Social Security Number detected",
        "guidance": "Sensitive identification must be protected with appropriate safeguards (Art. 32)"
    },
    "phone": {
        "pattern": r"\b(?:\+\d{1,3}\s?)?(?:\(?\d{2,4}\)?[\s.-]?)\d{3}[\s.-]?\d{3,4}[\s.-]?\d{3,4}\b",
        "severity": "MEDIUM",
        "article": "Art. 4, 6",
        "description": "Phone number detected",
        "guidance": "Phone numbers are personal data; ensure legal basis and transparency notices"
    },
    "iban": {
        "pattern": r"\b[A-Z]{2}\d{2}[A-Z0-9]{1,30}\b",
        "severity": "CRITICAL",
        "article": "Art. 4, 6, 32",
        "description": "IBAN detected",
        "guidance": "Bank account numbers are sensitive; use PCI-DSS compliant systems (Art. 32)"
    },
    "ip_address": {
        "pattern": r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b",
        "severity": "MEDIUM",
        "article": "Art. 4, 6",
        "description": "IP address detected",
        "guidance": "IP addresses are personal data under CJEU case law; collect with valid basis"
    },
    "mac_address": {
        "pattern": r"\b(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}\b",
        "severity": "MEDIUM",
        "article": "Art. 4, 6",
        "description": "MAC address detected",
        "guidance": "Device identifiers may be personal data; apply appropriate protections"
    },

    # Data Processing & Storage
    "data_storage": {
        "pattern": r"\b(localStorage|sessionStorage|IndexedDB|WebSQL|getItem|setItem|saveData|storeData|cache|persist|database\.save|db\.insert|memcache|redis\.set)\s*\(",
        "severity": "LOW",
        "article": "Art. 5, 32",
        "description": "Data storage detected",
        "guidance": "Verify stored data is necessary and encrypted (Art. 32); implement retention policies (Art. 5)"
    },

    # Tracking & Analytics
    "analytics_init": {
        "pattern": r"\b(gtag|ga|_gaq|analytics\.trackEvent|trackPageview|analytics\.pageview|mixpanel\.track|amplitude\.logEvent|datadog\.init|segment\.identify|ga4|google\.analytics)\s*\(",
        "severity": "CRITICAL",
        "article": "Art. 6, 7, ePrivacy Directive (2002/58/EC)",
        "description": "Analytics initialization without consent — violates ePrivacy Directive",
        "guidance": "Require explicit opt-in consent before any analytics initialization (Art. 7, ePrivacy Directive Art. 5)"
    },

    # Cookies & Tracking Technologies (SH6: extended libraries)
    "cookie_set": {
        "pattern": r"\b(document\.cookie|setCookie|setcookie|Set-Cookie|cookie\.set|cookies\.set)\s*[=:]",
        "severity": "MEDIUM",
        "article": "Art. 4, 6, 82, ePrivacy Directive (2002/58/EC)",
        "description": "Cookie being set",
        "guidance": "Require prior explicit consent for non-essential cookies (Art. 7, ePrivacy Directive)"
    },

    # Analytics SDK without consent check (SH9 escalation: CRITICAL)
    "analytics_sdk_init": {
        "pattern": r"\b(new\s+)?(?:GoogleAnalytics|Analytics|mixpanel|amplitude|segment|datadog|newrelic|splunk|dynatrace)\s*\(|window\[['\"](ga|_gaq|dataLayer)['\"]|require\s*\(\s*['\"]analytics['\"]\s*\)",
        "severity": "CRITICAL",
        "article": "Art. 6, 7, 13",
        "description": "Analytics SDK initialization without consent check detected",
        "guidance": "Wrap analytics initialization in consent check: if(user_consented_to_analytics) { ... }"
    },

    # Consent & Opt-out Patterns
    "consent_given": {
        "pattern": r"\b(user\.consent|userConsent|consentGiven|isConsented|hasConsent|consentStatus\s*===\s*['\"]yes['\"]|consentStatus\s*===\s*['\"]granted['\"])\b",
        "severity": "LOW",
        "article": "Art. 4, 7",
        "description": "Consent check detected",
        "guidance": "Ensure consent is freely given, specific, informed, and unambiguous (Art. 4.11, 7)"
    },
    "consent_missing": {
        "pattern": r"\b(trackEvent|logEvent|sendData|sendBeacon|fetch\s*\(|XMLHttpRequest|axios\.post|fetch|\.post\s*\()\s*\(",
        "severity": "LOW",
        "article": "Art. 6, 7",
        "description": "Data transmission without visible consent check",
        "guidance": "Verify that consent is obtained before transmitting user data"
    },
    "consent_no_withdraw": {
        "pattern": r"\b(consentGiven|userConsent|consentStatus)\s*=\s*(?:true|1|['\"]yes['\"]|['\"]granted['\"])\b",
        "severity": "LOW",
        "article": "Art. 7(3)",
        "description": "Consent set but no withdrawal mechanism visible",
        "guidance": "Art. 7(3) requires withdrawal mechanism as easy as giving consent"
    },
    "analytics_library": {
        "pattern": r"\b(?:" + "|".join(ANALYTICS_CONSENT_LIBRARIES) + r")\b",
        "severity": "LOW",
        "article": "Art. 6, 7, 13",
        "description": "Analytics/consent library detected",
        "guidance": "Verify library is configured correctly for GDPR compliance"
    },

    # User Rights & Mechanisms
    "data_export": {
        "pattern": r"\b(exportData|downloadData|dataExport|export_user_data|getPersonalData|export_profile|download_my_data)\b",
        "severity": "LOW",
        "article": "Art. 15, 20",
        "description": "Data export mechanism detected",
        "guidance": "Right of access (Art. 15) and data portability (Art. 20) implementation found"
    },
    "data_deletion": {
        "pattern": r"\b(deleteAccount|deleteUser|forgetMe|erasure|delete_personal_data|purgeData|gdpr_delete|right_to_be_forgotten)\b",
        "severity": "LOW",
        "article": "Art. 17",
        "description": "Data deletion mechanism detected",
        "guidance": "Right to erasure (Art. 17) implementation; verify cascading deletion"
    },
    "data_correction": {
        "pattern": r"\b(updateProfile|rectification|correct|editProfile|change_data|update_personal_data)\b",
        "severity": "LOW",
        "article": "Art. 16",
        "description": "Data correction mechanism detected",
        "guidance": "Right to rectification (Art. 16) implementation found"
    },

    # Third-Party & Data Sharing
    "third_party_api": {
        "pattern": r"\b(fetch|XMLHttpRequest|axios|$.ajax|$.get|request|https?://(?:[a-zA-Z0-9-]+\.)*(?:api\.|analytics\.|track\.|cdn\.))[a-zA-Z0-9-]*\.[a-z]{2,}",
        "severity": "MEDIUM",
        "article": "Art. 6, 28, 44",
        "description": "Third-party API call detected",
        "guidance": "Ensure data transfers to 3rd parties have legal basis (Art. 6) and are documented (Art. 28)"
    },
    "international_transfer": {
        "pattern": r"\b(transferToUS|sendToUS|cloudflare|aws\.amazonaws|gcp|azure|cloud\.google|s3\.amazonaws|international\.transfer|transfer_outside_eea)\b",
        "severity": "MEDIUM",
        "article": "Art. 44, 45, 46",
        "description": "International data transfer detected",
        "guidance": "Transfers outside EEA require adequacy (Art. 45), SCC (Art. 46), or BCR (Art. 47)"
    },

    # Sensitive Data (SH14: Add Art. 9)
    "health_data": {
        "pattern": r"\b(health|medical|diagnosis|treatment|prescription|vaccine|allergy|disability|medication|patient|hospital|clinic|mental_health)\b",
        "severity": "CRITICAL",
        "article": "Art. 9",
        "description": "Health-related data detected",
        "guidance": "Special category data (Art. 9) requires explicit consent (Art. 9.2.a) or legal exception"
    },
    "biometric_data": {
        "pattern": r"\b(fingerprint|facial|face|biometric|dna|iris|voice|recognition|faceapi|facedetection|faceidentification)\b",
        "severity": "CRITICAL",
        "article": "Art. 9",
        "description": "Biometric data detected",
        "guidance": "Biometric data (Art. 9) requires explicit consent or legal justification"
    },
    "genetic_data": {
        "pattern": r"\b(genetic|dna|gene|genomic|genome_sequence)\b",
        "severity": "CRITICAL",
        "article": "Art. 9",
        "description": "Genetic data detected",
        "guidance": "Genetic data (Art. 9) is special category; requires explicit consent"
    },
    "racial_ethnic": {
        "pattern": r"\b(race|ethnicity|ethnic|ethnic_origin|racial)\b",
        "severity": "CRITICAL",
        "article": "Art. 9",
        "description": "Racial/ethnic origin data detected",
        "guidance": "Special category (Art. 9); explicit consent or legal basis required"
    },
    "political_opinion": {
        "pattern": r"\b(political|party|vote|voting|election|campaign|partisan)\b",
        "severity": "CRITICAL",
        "article": "Art. 9",
        "description": "Political opinion data detected",
        "guidance": "Special category (Art. 9); explicit consent or legal basis required"
    },
    "religious_belief": {
        "pattern": r"\b(religion|religious|church|faith|creed|denomination)\b",
        "severity": "CRITICAL",
        "article": "Art. 9",
        "description": "Religious belief data detected",
        "guidance": "Special category (Art. 9); explicit consent or legal basis required"
    },
    "philosophical_belief": {
        "pattern": r"\b(philosophy|philosophical|belief|worldview|ideology)\b",
        "severity": "CRITICAL",
        "article": "Art. 9",
        "description": "Philosophical belief data detected",
        "guidance": "Special category (Art. 9); explicit consent or legal basis required"
    },
    "trade_union": {
        "pattern": r"\b(union|trade_union|labour_union|membership|collective)\b",
        "severity": "CRITICAL",
        "article": "Art. 9",
        "description": "Trade union membership data detected",
        "guidance": "Special category (Art. 9); explicit consent or legal basis required"
    },
    "sexual_orientation": {
        "pattern": r"\b(sexual|lgbtq|gay|lesbian|transgender|sexual_orientation)\b",
        "severity": "CRITICAL",
        "article": "Art. 9",
        "description": "Sexual orientation data detected",
        "guidance": "Special category (Art. 9); explicit consent or legal basis required"
    },
    "criminal_data": {
        "pattern": r"\b(conviction|offence|criminal|crime|arrest|prosecution)\b",
        "severity": "CRITICAL",
        "article": "Art. 10",
        "description": "Criminal conviction data detected",
        "guidance": "Art. 10 prohibits processing except by authorized processors under legal authority"
    },

    # Data Protection Officer & Accountability
    "dpo_contact": {
        "pattern": r"\b(dpo|data_protection_officer|dpo@|datenschutz|cil|chief_information_officer)\b",
        "severity": "LOW",
        "article": "Art. 37",
        "description": "DPO contact information detected",
        "guidance": "Art. 37 may require DPO appointment; contact info should be public"
    },
    "legal_basis": {
        "pattern": r"\b(legalBasis|legal_basis|basis_for_processing|article_6|consentRequired|legitimateInterest|publicTask)\b",
        "severity": "LOW",
        "article": "Art. 6",
        "description": "Legal basis reference detected",
        "guidance": "Ensure processing has documented legal basis (Art. 6)"
    },

    # Data Retention
    "retention_policy": {
        "pattern": r"\b(retention|retentionDays|retentionPeriod|deleteAfter|ttl|expiresAt|purgeAfter|maxAge|keepFor)\b",
        "severity": "LOW",
        "article": "Art. 5(1)(e)",
        "description": "Data retention policy detected",
        "guidance": "Storage limitation principle (Art. 5); implement automated deletion"
    },

    # Children's Data (COPPA, GDPR Art. 8)
    "child_age_gate": {
        "pattern": r"\b(ageGate|ageCheck|isAdult|isMinor|ageVerification|age_over_13|age_over_16|age_of_consent|coppa)\b",
        "severity": "MEDIUM",
        "article": "Art. 8",
        "description": "Child data protection mechanism detected",
        "guidance": "Art. 8: children under 16 require parental consent (or lower per Member State)"
    },

    # Processor Agreement & DPA
    "processor_agreement": {
        "pattern": r"\b(DPA|data_processor|processor_agreement|data_processing_agreement|sub_processor|subprocessor|processor_authorized)\b",
        "severity": "LOW",
        "article": "Art. 28",
        "description": "Data Processor Agreement reference detected",
        "guidance": "Art. 28 requires written DPA with all processors; ensure sub-processor list"
    },

    # Joint Controller (SH15: new escalation trigger)
    "joint_controller": {
        "pattern": r"\b(joint_controller|joint_processing|joint_control|controller_and_processor|co_controller|shared_responsibility)\b",
        "severity": "MEDIUM",
        "article": "Art. 26",
        "description": "Joint controller arrangement detected",
        "guidance": "Art. 26 requires arrangement with joint controller defining responsibilities"
    },

    # EU Representative (SH16: new escalation trigger)
    "eu_representative": {
        "pattern": r"\b(eu_representative|representative_in_union|eea_representative|gdpr_representative|representative@|data\.protection)\b",
        "severity": "MEDIUM",
        "article": "Art. 27",
        "description": "EU representative reference detected",
        "guidance": "Art. 27: non-EU controllers may need EU representative"
    },

    # DPO Required (SH17: new escalation trigger)
    "dpo_required": {
        "pattern": r"\b(dpo_required|appoint_dpo|must_appoint_dpo|controller_type_public|large_scale_monitoring|systematic_monitoring)\b",
        "severity": "MEDIUM",
        "article": "Art. 37",
        "description": "DPO appointment potentially required",
        "guidance": "Art. 37: public authorities and large-scale monitoring may require DPO"
    },

    # Profiling & Automated Decision-Making
    "profiling": {
        "pattern": r"\b(profiling|profile|segment|personalize|recommendation|predict|ml_model|ai_model|decision_tree|neural_network|clustering)\b",
        "severity": "MEDIUM",
        "article": "Art. 4(4), 22",
        "description": "User profiling detected",
        "guidance": "Profiling (Art. 4) and automated decisions (Art. 22) require transparency notices"
    },
    "automated_decision": {
        "pattern": r"\b(automated_decision|automate_decision|automated_processing|sole_automated|decision_based_on|auto_deny|auto_approve)\b",
        "severity": "MEDIUM",
        "article": "Art. 22",
        "description": "Automated decision-making detected",
        "guidance": "Art. 22: automated decisions that affect legal/similar effect need safeguards"
    },

    # Privacy by Design & Data Minimization
    "encryption": {
        "pattern": r"\b(encrypt|encrypted|crypto|cipher|aes|rsa|tls|ssl|hash|bcrypt|pbkdf2|scrypt|argon2)\b",
        "severity": "LOW",
        "article": "Art. 32, 25",
        "description": "Encryption detected",
        "guidance": "Good: encryption is part of data protection by design (Art. 25, 32)"
    },
    "anonymization": {
        "pattern": r"\b(anonymize|anonymized|deidentify|pseudo|pseudonymize|de_identify|irreversible|anonymization|anonymized_data)\b",
        "severity": "LOW",
        "article": "Art. 4, 11, 32",
        "description": "Anonymization detected",
        "guidance": "True anonymization exempts data from GDPR; pseudonymization still requires protection"
    },

    # Breach Notification
    "breach_notification": {
        "pattern": r"\b(breach_notification|notifyBreach|breachNotice|data_breach|security_incident|incident_report|notify_dpa)\b",
        "severity": "LOW",
        "article": "Art. 33, 34",
        "description": "Breach notification mechanism detected",
        "guidance": "Art. 33: notify supervisory authority within 72h; Art. 34: notify affected persons"
    },
}

# ─── Pattern Compilation ──────────────────────────────────────────────────────

# Pre-compile patterns with error handling (SH6)
COMPILED_PATTERNS = {}
for rule_name, rule in PATTERNS.items():
    try:
        COMPILED_PATTERNS[rule_name] = {
            "compiled": re.compile(rule["pattern"], re.IGNORECASE | re.MULTILINE),
            "severity": rule["severity"],
            "article": rule["article"],
            "description": rule["description"],
            "guidance": rule["guidance"],
        }
    except re.error as e:
        print(f"WARNING: Failed to compile pattern '{rule_name}': {e}", file=sys.stderr)
        continue

# Art. 9 patterns for special category detection (SH14)
ART9_PATTERNS = {
    "health_data", "biometric_data", "genetic_data", "racial_ethnic",
    "political_opinion", "religious_belief", "philosophical_belief",
    "trade_union", "sexual_orientation",
}

# ─── GDPRScanner Class ────────────────────────────────────────────────────────

class GDPRScanner:
    def __init__(self, project_path, module_path=None):
        self.project_path = Path(project_path).resolve()
        self.module_path = Path(module_path).resolve() if module_path else self.project_path
        self.findings = []
        self.scanned_files = 0
        self.start_time = time.monotonic()

    def scan(self):
        """Main entry point for scanning."""
        project_context = self._detect_project_context()
        locales = self._detect_locales()
        self._walk_and_scan()
        self._scan_dependencies()
        self._check_missing_mechanisms()
        elapsed = time.monotonic() - self.start_time
        return self._build_output(project_context, locales, elapsed)

    def _detect_project_context(self):
        """Detect project type from configuration files."""
        context = {"type": "unknown", "frameworks": [], "has_package_json": False}

        for filename in ["package.json", "pyproject.toml", "pom.xml", "Gemfile", "go.mod", "Cargo.toml"]:
            if (self.project_path / filename).exists():
                if filename == "package.json":
                    context["has_package_json"] = True
                    try:
                        with open(self.project_path / filename) as f:
                            pkg = json.load(f)
                            if "dependencies" in pkg or "devDependencies" in pkg:
                                deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
                                if "react" in deps: context["frameworks"].append("React")
                                if "vue" in deps: context["frameworks"].append("Vue")
                                if "svelte" in deps: context["frameworks"].append("Svelte")
                                if "next" in deps: context["frameworks"].append("Next.js")
                                if "nuxt" in deps: context["frameworks"].append("Nuxt")
                                if "express" in deps: context["frameworks"].append("Express")
                                if "django" in deps: context["frameworks"].append("Django")
                    except (json.JSONDecodeError, IOError):
                        pass

        return context

    def _detect_locales(self):
        """Detect supported locales from i18n files."""
        locales = set()
        for root, dirs, files in os.walk(self.module_path):
            # Skip unwanted directories
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]

            for file in files:
                if any(marker in root.lower() for marker in I18N_FILE_MARKERS):
                    if file.endswith(('.json', '.yaml', '.yml', '.ts', '.js')):
                        try:
                            match = re.search(r'(?:en|de|fr|es|it|pl|cs|hu|ro|sk)-?[A-Z]{2}?|[a-z]{2}(?:[_-][A-Z]{2})?', file)
                            if match:
                                locales.add(match.group(0))
                        except:
                            pass

        return sorted(list(locales)) if locales else ["en"]

    def _walk_and_scan(self):
        """Walk project directory and scan files."""
        for root, dirs, files in os.walk(self.module_path):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]

            for file in files:
                file_path = Path(root) / file

                # Skip config files
                if file in SKIP_CONFIG_FILES:
                    continue

                # Check if file extension is scannable
                if file_path.suffix not in SCAN_EXTENSIONS:
                    continue

                self._scan_file(file_path)

    def _scan_file(self, file_path):
        """Scan a single file for GDPR patterns."""
        self.scanned_files += 1

        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except (IOError, OSError):
            return

        lines = content.split('\n')

        # Detect if file is test/fixture/config/spec
        is_test_file = any(marker in file_path.name for marker in TEST_FILE_MARKERS)
        is_config_file = any(marker in file_path.name.lower() or marker in str(file_path).lower()
                            for marker in CONFIG_SPEC_TEST_PATTERNS)
        is_i18n_file = any(marker in str(file_path).lower() for marker in I18N_FILE_MARKERS)

        # Track findings per rule per file
        findings_per_rule = {}

        for rule_name, rule in COMPILED_PATTERNS.items():
            try:
                matches = list(rule["compiled"].finditer(content))
            except Exception as e:
                continue

            if not matches:
                continue

            for match in matches:
                # Max 10 findings per rule per file
                if findings_per_rule.get(rule_name, 0) >= 10:
                    continue

                line_num = content[:match.start()].count('\n') + 1

                # Skip test values for email/credit_card/ssn/phone/iban patterns
                matched_text = match.group(0)
                if rule_name in {"email", "credit_card", "ssn", "phone", "iban"}:
                    if any(test_val.lower() in matched_text.lower() for test_val in TEST_VALUES):
                        continue

                severity = rule["severity"]

                # Downgrade severity for test files (SH4)
                if is_test_file:
                    if severity == "CRITICAL":
                        severity = "HIGH"
                    elif severity == "HIGH":
                        severity = "MEDIUM"

                # Downgrade to LOW for i18n files and consent-related findings
                if is_i18n_file and "consent" in rule_name:
                    severity = "LOW"

                # Special logic for consent_no_withdraw: check 5-line context window (SH8)
                if rule_name == "consent_no_withdraw":
                    # Check if withdraw/revoke mechanism exists nearby (5-line context)
                    context_start = max(0, line_num - 6)
                    context_end = min(len(lines), line_num + 4)
                    context_text = "\n".join(lines[context_start:context_end])
                    if re.search(r'\b(withdraw|revoke|remove_consent|consent_withdrawn|consent_revoked)\b', context_text, re.IGNORECASE):
                        continue

                # Create finding
                finding = {
                    "rule": rule_name,
                    "file": str(file_path.relative_to(self.project_path)),
                    "line": line_num,
                    "severity": severity,
                    "article": rule["article"],
                    "description": rule["description"],
                    "snippet": matched_text[:100],
                    "guidance": rule["guidance"],
                }

                # Dedup by file + rule + line
                dedup_key = (finding["file"], finding["rule"], finding["line"])
                if not any(
                    (f["file"] == finding["file"] and f["rule"] == finding["rule"] and f["line"] == finding["line"])
                    for f in self.findings
                ):
                    self.findings.append(finding)

                findings_per_rule[rule_name] = findings_per_rule.get(rule_name, 0) + 1

    def _scan_dependencies(self):
        """Check for package.json dependencies."""
        package_json = self.project_path / "package.json"

        if not package_json.exists():
            return

        try:
            with open(package_json) as f:
                pkg = json.load(f)
        except (json.JSONDecodeError, IOError):
            return

        deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}

        for lib in ANALYTICS_CONSENT_LIBRARIES:
            if lib in deps:
                self.findings.append({
                    "rule": "analytics_library",
                    "file": "package.json",
                    "line": 0,
                    "severity": "LOW",
                    "article": "Art. 6, 7, 13",
                    "description": f"Consent library '{lib}' found in dependencies",
                    "snippet": f"{lib}@{deps[lib]}",
                    "guidance": "Verify library is properly configured for GDPR compliance"
                })

    def _check_missing_mechanisms(self):
        """Check for missing GDPR mechanisms."""
        has_dpo = any(f["rule"] == "dpo_contact" for f in self.findings)
        has_retention = any(f["rule"] == "retention_policy" for f in self.findings)
        has_breach_notification = any(f["rule"] == "breach_notification" for f in self.findings)
        has_consent = any("consent" in f["rule"] for f in self.findings)

        if not has_dpo:
            self.findings.append({
                "rule": "missing_dpo_contact",
                "file": "N/A",
                "line": 0,
                "severity": "LOW",
                "article": "Art. 37",
                "description": "No DPO contact information found",
                "snippet": "N/A",
                "guidance": "If DPO is required, provide public contact information"
            })

        if not has_retention:
            self.findings.append({
                "rule": "missing_retention_policy",
                "file": "N/A",
                "line": 0,
                "severity": "LOW",
                "article": "Art. 5(1)(e)",
                "description": "No data retention policy detected",
                "snippet": "N/A",
                "guidance": "Implement automated data deletion based on retention periods"
            })

    def _build_output(self, project_context, locales, elapsed_seconds):
        """Build JSON output."""
        # Severity scoring
        severity_scores = {"CRITICAL": -15, "HIGH": -5, "MEDIUM": -1, "LOW": -0.1}
        score = sum(severity_scores.get(f["severity"], 0) for f in self.findings)
        score = max(0, score)  # Cap at 0

        # Score label
        critical_count = sum(1 for f in self.findings if f["severity"] == "CRITICAL")
        high_count = sum(1 for f in self.findings if f["severity"] == "HIGH")
        medium_count = sum(1 for f in self.findings if f["severity"] == "MEDIUM")

        if critical_count >= 1 or high_count >= 3:
            score_label = "RED"
        elif high_count >= 1 or medium_count >= 4:
            score_label = "YELLOW"
        else:
            score_label = "GREEN"

        return {
            "scan_metadata": {
                "scanner_version": SCANNER_VERSION,
                "scan_timestamp": datetime.now(timezone.utc).isoformat(),
                "project_path": str(self.project_path),
                "module_path": str(self.module_path),
                "scanned_files": self.scanned_files,
                "elapsed_seconds": round(elapsed_seconds, 2),
                "project_context": project_context,
                "supported_locales": locales,
            },
            "summary": {
                "total_findings": len(self.findings),
                "critical": critical_count,
                "high": high_count,
                "medium": medium_count,
                "low": sum(1 for f in self.findings if f["severity"] == "LOW"),
                "compliance_score": score,
                "compliance_label": score_label,
            },
            "findings": sorted(self.findings, key=lambda f: (
                {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}.get(f["severity"], 4),
                f["file"],
                f["line"]
            )),
            "guidance": {
                "next_steps": [
                    "Fix CRITICAL findings immediately (compliance breach)",
                    "Address HIGH findings within 30 days (significant risk)",
                    "Remediate MEDIUM findings within 90 days (recommended)",
                    "Review LOW findings for best practices",
                ] if score_label == "RED" else [
                    "Review findings for compliance improvements",
                    "Implement consent mechanisms if needed",
                    "Document legal basis for data processing",
                ],
                "resources": [
                    "GDPR Full Text: https://gdpr-info.eu/",
                    "Article 29 Working Party Guidelines: https://ec.europa.eu/justice/article-29/",
                    "ePrivacy Directive (2002/58/EC): https://eur-lex.europa.eu/legal-content/en/ALL/?uri=CELEX:32002L0058",
                    "Creativa Legal: https://creativa.legal/",
                ]
            }
        }

# ─── Main Entry Point ────────────────────────────────────────────────────────

def main():
    import argparse

    parser = argparse.ArgumentParser(description="GDPR Compliance Scanner")
    parser.add_argument("project_path", help="Path to project root")
    parser.add_argument("--module", help="Subdirectory to scan (for monorepos)")
    args = parser.parse_args()

    if not os.path.isdir(args.project_path):
        print(f"Error: Project path '{args.project_path}' does not exist", file=sys.stderr)
        sys.exit(1)

    module_path = args.module if args.module else None
    scanner = GDPRScanner(args.project_path, module_path)
    result = scanner.scan()
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
