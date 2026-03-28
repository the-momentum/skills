# OpenGDPR v0.5.0

**GDPR Compliance Scanner for Claude Code**

Author: [Creativa Legal](https://www.creativa.legal) | Tested by: [Momentum](https://www.themomentum.ai) | License: GNU GPLv3

## What is OpenGDPR?

A Claude Code skill that automatically scans application source code for GDPR (EU Regulation 2016/679) compliance issues. It uses a deterministic Python regex scanner (no external dependencies) to detect personal data patterns, risky practices, and missing GDPR mechanisms.

## v0.5.0 Changes (Legal Review)

- Enhanced disclaimers and Terms of Use (5-point liability clause)
- ePrivacy Directive (2002/58/EC) references for cookie/tracking compliance
- Analytics without consent → CRITICAL severity (ePrivacy violation)
- New escalation triggers: Art. 26 (joint controllers), Art. 27 (EU representatives), Art. 37 (DPO required)
- Added "philosophical beliefs" and "sex life" to Art. 9 special categories
- Removed timelines from severity levels (reaction time depends on project)
- Restructured Legal Basis table: Art. 6 + Art. 9(2)(a-j) + Art. 10 in single table
- Removed non-existent Art. 45(g) from penalty tiers
- Added adequacy countries: Andorra, Argentina, Brazil, Uruguay
- 288 checkpoints across 21 sections (was 282/20)
- Elapsed time measurement in scanner output
- Version string bug fixed (uses SCANNER_VERSION variable)

## Structure

```
openGDPR/
├── SKILL.md                          # Main skill definition
├── README.md                         # This file
├── scripts/
│   └── scan_codebase.py              # Deterministic regex scanner (stdlib only)
├── references/
│   ├── gdpr-reference-tables.md      # Legal basis, categories, transfer mechanisms
│   ├── gdpr-checklist.md             # 288 checkpoints in 21 sections
│   └── report-template.md            # Report generation template
└── assets/
    └── gdpr-severity-matrix.json     # Severity levels, scoring, escalation triggers
```

## Usage

```bash
# Mode A: Code Scan
python scripts/scan_codebase.py /path/to/project --pretty

# With monorepo module
python scripts/scan_codebase.py /path/to/monorepo --module apps/backend --pretty
```

## Disclaimer

This tool identifies potential technical compliance issues. It does NOT constitute legal advice and does NOT replace a legal audit. For professional GDPR consultation, contact [Creativa Legal](https://www.creativa.legal).
