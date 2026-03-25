# GDPR Compliance Checklist v0.5.0
## EU Regulation 2016/679 — 288 Checkpoints in 21 Sections

**OpenGDPR by Creativa Legal** — www.creativa.legal | **Tested by Momentum** — www.themomentum.ai

**Instructions for Mode B/C**: Claude evaluates all ~288 checkpoints based on interview answers and code scan results. Present only gaps, issues, and warnings — not the full list. Use ✅ / ❌ / ⚠️ / N/A per item.

---

## Section 1 — Legal Basis for Processing (Art. 6) [20 pts]

□ 1.1 Each type of personal data has a documented legal basis
□ 1.2 Consent (Art. 6(1)(a)): freely given, specific, informed, unambiguous
□ 1.3 Contract (Art. 6(1)(b)): processing necessary for contract with the data subject
□ 1.4 Legal obligation (Art. 6(1)(c)): identified and documented
□ 1.5 Vital interests (Art. 6(1)(d)): only used when truly applicable
□ 1.6 Public task (Art. 6(1)(e)): applicable only for public authorities
□ 1.7 Legitimate interests (Art. 6(1)(f)): LIA (Legitimate Interests Assessment) documented
□ 1.8 Legitimate interest does not override data subject rights (balancing test done)
□ 1.9 Legal basis documented before processing starts, not retroactively
□ 1.10 Different legal bases used for different processing activities
□ 1.11 Legal basis for secondary processing identified separately
□ 1.12 Legal basis communicated to data subjects (Art. 13/14)
□ 1.13 Marketing processing uses consent, not legitimate interest (country-specific rules)
□ 1.14 Profiling legal basis identified separately from core processing
□ 1.15 Legal basis re-evaluated when processing purpose changes
□ 1.16 Purpose limitation respected — data not used for incompatible new purposes
□ 1.17 No "bundled" consent covering multiple purposes simultaneously
□ 1.18 Employee monitoring legal basis identified (consent rarely valid for employees)
□ 1.19 Children's data: parental consent mechanism in place (Art. 8)
□ 1.20 Processing register (Art. 30) includes legal basis for each activity

## Section 2 — Consent Management (Art. 7) [18 pts]

□ 2.1 Consent request is clear, plain language, distinguishable from other matters
□ 2.2 Consent is not a condition for service (unless strictly necessary)
□ 2.3 Granular consent — separate for each purpose (analytics, marketing, profiling)
□ 2.4 No pre-ticked checkboxes
□ 2.5 Opt-in mechanism (not opt-out) for marketing
□ 2.6 Consent timestamp recorded with version of consent text shown
□ 2.7 Withdrawal mechanism as easy as giving consent
□ 2.8 Withdrawal does not affect lawfulness of prior processing
□ 2.9 Withdrawal immediately stops processing for that purpose
□ 2.10 Consent records retained as long as necessary to demonstrate compliance
□ 2.11 Cookie consent: non-essential cookies not set before consent
□ 2.12 Cookie consent: categories explained (strictly necessary, analytics, marketing)
□ 2.13 Cookie consent: no cookie walls (access not conditional on consent)
□ 2.14 Cookie consent refresh — users can change preferences
□ 2.15 Re-consent collected when purpose changes or consent expires
□ 2.16 Consent by children: parental consent verified for under-16 (member state may lower to 13)
□ 2.17 Implied consent NOT used for cookies or tracking
□ 2.18 "Scrolling" or "continued use" NOT treated as consent

## Section 3 — Privacy Notice / Transparency (Art. 13-14) [20 pts]

□ 3.1 Privacy notice provided at time of data collection (Art. 13)
□ 3.2 Privacy notice for indirectly collected data within 1 month (Art. 14)
□ 3.3 Identity and contact details of controller provided
□ 3.4 DPO contact details provided (if applicable)
□ 3.5 Purposes of processing described for each data type
□ 3.6 Legal basis for each purpose stated
□ 3.7 Legitimate interests described (if used as basis)
□ 3.8 Recipients or categories of recipients listed
□ 3.9 Transfers outside EEA disclosed with safeguards identified
□ 3.10 Retention periods or criteria for determining them stated
□ 3.11 All eight data subject rights listed (Art. 15-22)
□ 3.12 Right to withdraw consent mentioned (where consent is basis)
□ 3.13 Right to lodge complaint with supervisory authority mentioned
□ 3.14 Whether provision of data is contractual/statutory/necessary stated
□ 3.15 Existence of automated decision-making disclosed (Art. 22)
□ 3.16 Privacy notice in plain language, accessible to target audience
□ 3.17 Privacy notice accessible at all times (not just during registration)
□ 3.18 Privacy notice updated and version-controlled
□ 3.19 Children's privacy notice uses age-appropriate language
□ 3.20 Layered notice approach used (summary + full version)

## Section 4 — Data Subject Rights (Art. 15-22) [22 pts]

□ 4.1 Right of access (Art. 15): mechanism to fulfill requests within 30 days
□ 4.2 Access response includes all required information (Art. 15(1)(a)-(h))
□ 4.3 Right to rectification (Art. 16): mechanism for users to correct data
□ 4.4 Right to erasure (Art. 17): hard-delete capability for all data stores
□ 4.5 Right to erasure: backup deletion scheduled and documented
□ 4.6 Right to erasure: cascading deletion across related records
□ 4.7 Right to restrict processing (Art. 18): technical mechanism exists
□ 4.8 Restriction notified to third parties who received the data
□ 4.9 Right to data portability (Art. 20): export in machine-readable format (JSON/CSV/XML)
□ 4.10 Portability covers data provided by the subject AND data observed (behavior)
□ 4.11 Right to object (Art. 21): mechanism for direct marketing opt-out
□ 4.12 Right to object to profiling: technical mechanism
□ 4.13 Right to not be subject to automated decisions (Art. 22): human review option
□ 4.14 All requests acknowledged immediately, fulfilled within 30 days
□ 4.15 Extension to 90 days (complex cases): subject notified within 30 days
□ 4.16 Identity verification before fulfilling requests (without excessive friction)
□ 4.17 DSR (Data Subject Request) tracking system exists
□ 4.18 Third parties notified of erasure/rectification requests (Art. 19)
□ 4.19 Requests fulfilled free of charge (fees only for manifestly unfounded/excessive)
□ 4.20 Refusal documented with grounds and subject notified of complaint right
□ 4.21 DSR workflow tested at least annually
□ 4.22 DSR response template prepared in user's language

## Section 5 — Privacy by Design & Default (Art. 25) [15 pts]

□ 5.1 Privacy considerations included in system design from the start
□ 5.2 Data minimization: only data necessary for stated purpose collected
□ 5.3 Purpose limitation enforced technically, not just by policy
□ 5.4 Default settings are the most privacy-protective option
□ 5.5 Pseudonymization used where possible (Art. 4(5))
□ 5.6 Encryption used for data at rest and in transit
□ 5.7 Access controls enforce minimum necessary access
□ 5.8 Data retention enforced automatically, not just by policy
□ 5.9 Third-party components audited for privacy compliance before integration
□ 5.10 Privacy review included in development/deployment checklist
□ 5.11 Aggregation/anonymization used for analytics instead of raw PII
□ 5.12 Separation between production and test environments (no real data in tests)
□ 5.13 Privacy impact considered for new features before release
□ 5.14 API response filtering — only requested/authorized data returned
□ 5.15 PII excluded from URLs, query strings, and resource names

## Section 6 — Data Security (Art. 32) [18 pts]

□ 6.1 Encryption at rest: AES-256 or equivalent for databases and file storage
□ 6.2 Encryption in transit: TLS 1.2 minimum, TLS 1.3 preferred
□ 6.3 Passwords hashed with Argon2id, bcrypt (≥10 rounds), or PBKDF2 (600k+ iterations)
□ 6.4 Unique user identification — no shared accounts
□ 6.5 Role-based access control (RBAC) with minimum necessary principle
□ 6.6 Multi-factor authentication for admin and high-privilege access
□ 6.7 Session timeout configured appropriately (15 min for sensitive systems)
□ 6.8 Account lockout after failed attempts (3-6 attempts, 15-30 min lockout)
□ 6.9 Audit logs for all PHI/PII access (who, what, when)
□ 6.10 Audit logs write-once / tamper-evident
□ 6.11 Audit log retention ≥ 5 years (varies by sector)
□ 6.12 No PII in log files, error messages, or stack traces
□ 6.13 No credentials hardcoded in source code or config files
□ 6.14 Credentials stored in secrets manager (not environment variables in plain config)
□ 6.15 Regular vulnerability scanning (every 6 months minimum)
□ 6.16 Penetration testing (annually minimum)
□ 6.17 Security headers configured (HSTS, CSP, X-Frame-Options, etc.)
□ 6.18 CORS restricted to specific origins (no wildcard with credentials)

## Section 7 — Data Breach (Art. 33-34) [12 pts]

□ 7.1 Incident detection capability in place (monitoring, alerting)
□ 7.2 Breach response procedure documented and tested
□ 7.3 72-hour notification procedure to supervisory authority (Art. 33)
□ 7.4 Supervisory authority contact information documented
□ 7.5 Art. 33(3) notification content checklist available
□ 7.6 High-risk breach: procedure to notify affected individuals without undue delay (Art. 34)
□ 7.7 Breach register maintained (including "near misses")
□ 7.8 Breach categories defined (what constitutes a reportable breach)
□ 7.9 Third-party breach notification obligations in contracts (sub-processor → processor → controller)
□ 7.10 Breach simulation/tabletop exercise conducted (at least annually)
□ 7.11 Post-breach remediation process documented
□ 7.12 Legal team and DPO included in breach response chain

## Section 8 — Processing Register (Art. 30) [10 pts]

□ 8.1 Record of processing activities (RoPA) exists and is maintained
□ 8.2 RoPA includes: controller identity, purposes, categories of data, recipients
□ 8.3 RoPA includes: transfers to third countries with safeguards
□ 8.4 RoPA includes: retention periods for each processing activity
□ 8.5 RoPA includes: security measures (general description)
□ 8.6 RoPA updated when new processing activities are introduced
□ 8.7 RoPA available to supervisory authority on request
□ 8.8 Processor RoPA maintained (if acting as processor)
□ 8.9 RoPA reviewed and validated at least annually
□ 8.10 RoPA covers processing by all systems (not just main app)

## Section 9 — Data Protection Officer (Art. 37-39) [8 pts]

□ 9.1 DPO designation assessed (mandatory for: public authorities; large-scale systematic monitoring; large-scale special category data)
□ 9.2 DPO appointed if required (or documented decision not to appoint)
□ 9.3 DPO contact details published in privacy notice
□ 9.4 DPO registered with supervisory authority (required in some member states)
□ 9.5 DPO has adequate resources and access to management
□ 9.6 DPO independent (not involved in processing decisions)
□ 9.7 DPO consulted for DPIA, breach response, and new processing activities
□ 9.8 DPO contact point for data subjects and supervisory authority

## Section 10 — Joint Controllers (Art. 26) [6 pts]

□ 10.1 Joint controller arrangements identified and documented in writing
□ 10.2 Joint controller agreement specifies respective responsibilities and transparency obligations
□ 10.3 Joint controller agreement defines mechanism for data subject requests (single or multiple points)
□ 10.4 Both controllers acknowledge liability for joint processing
□ 10.5 Joint controller status disclosed to data subjects in privacy notice
□ 10.6 Processing register includes joint controller relationships and data sharing terms

## Section 11 — DPIA (Art. 35) [10 pts]

□ 11.1 DPIA triggers assessed: large-scale processing, systematic monitoring, special category data, innovative technology, public spaces
□ 11.2 DPIA conducted where required before processing begins
□ 11.3 DPIA includes: systematic description of processing and purposes
□ 11.4 DPIA includes: necessity and proportionality assessment
□ 11.5 DPIA includes: risks to rights and freedoms of individuals
□ 11.6 DPIA includes: measures to address risks
□ 11.7 DPO consulted in DPIA process
□ 11.8 High-risk processing: supervisory authority consulted (Art. 36) before start
□ 11.9 DPIA reviewed when processing significantly changes
□ 11.10 DPIA documentation retained

## Section 12 — International Transfers (Art. 44-49) [12 pts]

□ 12.1 Transfers outside EEA identified (including via cloud providers, CDNs, analytics)
□ 12.2 Adequacy decisions checked for destination countries (Art. 45)
□ 12.3 Standard Contractual Clauses (SCCs) in place where no adequacy decision
□ 12.4 SCCs: updated 2021 versions used (old versions phased out)
□ 12.5 Binding Corporate Rules (BCRs) in place for intra-group transfers (if applicable)
□ 12.6 Transfer Impact Assessment (TIA) conducted where required (post-Schrems II)
□ 12.7 Supplementary technical measures applied if third country lacks equivalent protection
□ 12.8 US transfers: EU-US Data Privacy Framework adequacy verified (or SCCs used)
□ 12.9 Third-party SDKs (analytics, advertising) audited for EEA data export
□ 12.10 Privacy notice discloses all transfer destinations and safeguards
□ 12.11 Sub-processors in third countries covered by appropriate safeguards
□ 12.12 Data localization requirements assessed (some member states have sector-specific rules)

## Section 13 — Controller / Processor Agreements (Art. 28) [10 pts]

□ 13.1 All processors identified (cloud providers, SaaS vendors, analytics, support tools)
□ 13.2 DPA (Data Processing Agreement) in place with each processor
□ 13.3 DPA includes all Art. 28(3) mandatory clauses
□ 13.4 Sub-processor authorization mechanism in DPAs
□ 13.5 Processor instructed in writing for all processing activities
□ 13.6 Processor deletion/return of data upon contract termination
□ 13.7 Processor audit rights included in DPA
□ 13.8 Joint controller arrangements identified and documented (Art. 26)
□ 13.9 DPAs reviewed after processor changes (new sub-processors, service changes)
□ 13.10 List of processors/sub-processors maintained and accessible to data subjects

## Section 14 — Special Categories of Data (Art. 9) [12 pts]

□ 14.1 Special category data identified: health, biometric, genetic, racial/ethnic, political, religious, trade union, sexual orientation
□ 14.2 Explicit consent obtained for Art. 9 processing (or other Art. 9(2) exception applies)
□ 14.3 Processing strictly limited to stated purpose
□ 14.4 Enhanced security for special category data (separate encryption key, stricter access)
□ 14.5 Access log for special category data: every access recorded
□ 14.6 Separate legal basis for processing + additional condition under Art. 9(2)
□ 14.7 Health data: processed only by health professionals or under obligation of secrecy
□ 14.8 DPIA conducted (required for large-scale processing of Art. 9 data)
□ 14.9 Special category data not used for automated decisions without explicit consent
□ 14.10 Retention minimized — deleted when no longer necessary
□ 14.11 Art. 9 data not shared with processors without specific authorization
□ 14.12 Children's special category data: heightened protection applied

## Section 15 — Criminal Data (Art. 10) [6 pts]

□ 15.1 Criminal data identified in systems (convictions, offences, criminal record)
□ 15.2 Processing only under official authority or with specific national law authorization
□ 15.3 No criminal data processing without documented legal basis (Art. 10 stricter than Art. 9)
□ 15.4 Criminal data stored only as long as strictly necessary
□ 15.5 Access to criminal data restricted to authorized personnel only
□ 15.6 Processing of criminal data disclosed in privacy notice

## Section 16 — Automated Decisions & Profiling (Art. 22) [10 pts]

□ 16.1 Automated decision-making identified (credit scoring, hiring, insurance, access control)
□ 16.2 Profiling activities identified and documented
□ 16.3 Legal basis: consent, contract, or EU/member state law (Art. 22(2))
□ 16.4 Data subjects informed of automated decision-making (Art. 13/14)
□ 16.5 Right to human review mechanism in place
□ 16.6 Right to express point of view implemented
□ 16.7 Right to contest the decision implemented
□ 16.8 Logic of automated decision explained to data subjects on request
□ 16.9 Automated decisions not based solely on special category data (unless Art. 9(2)(a))
□ 16.10 Regular review of automated decision models for bias and accuracy

## Section 17 — Children's Data (Art. 8) [8 pts]

□ 17.1 Age of digital consent assessed per member state (13-16 years)
□ 17.2 Age verification mechanism in place
□ 17.3 Parental consent collection and verification process exists
□ 17.4 Privacy notice uses child-appropriate language
□ 17.5 Children's data not used for profiling or behavioral advertising
□ 17.6 Enhanced protection for children's data (extra security, limited retention)
□ 17.7 Parental consent withdrawal mechanism exists
□ 17.8 Children's data not shared with third parties without parental consent

## Section 18 — Data Retention (Art. 5(1)(e)) [10 pts]

□ 18.1 Retention schedule defined for each type of personal data
□ 18.2 Retention periods justified by purpose or legal obligation
□ 18.3 Automated deletion enforced technically (not just policy)
□ 18.4 Backup retention aligned with data deletion (data deleted from backups too)
□ 18.5 Logs containing PII have defined retention period (max 1-2 years typical)
□ 18.6 Soft-delete records have scheduled hard-delete (30-90 days typical)
□ 18.7 Archived data reviewed periodically for continued necessity
□ 18.8 Legal holds process: suspend deletion when required for litigation/investigation
□ 18.9 Retention schedule documented in processing register (Art. 30)
□ 18.10 Users informed of retention periods in privacy notice

## Section 19 — Third-Party Integrations & ePrivacy [10 pts]

□ 19.1 All third-party services receiving PII identified
□ 19.2 Analytics SDKs (GA, Mixpanel, Amplitude) audited for consent requirement
□ 19.3 Analytics not loaded before consent obtained
□ 19.4 Social media plugins (Facebook, Twitter) audited for consent requirement
□ 19.5 CRM integration: DPA with CRM provider in place
□ 19.6 Email service: DPA in place, PII not in email subjects/headers
□ 19.7 Support tools (Intercom, Zendesk): DPA in place, agents trained on GDPR
□ 19.8 Payment processor: PCI-DSS compliant + GDPR DPA
□ 19.9 Cloud provider: DPA in place (BAA if EU health data)
□ 19.10 ePrivacy compliance: cookies and tracking governed by Directive 2002/58/EC (Art. 5-7, Art. 13-14)

## Section 20 — Staff Training & Governance [8 pts]

□ 20.1 GDPR training provided to all staff handling personal data
□ 20.2 Training records maintained (who, when, which version)
□ 20.3 Annual refresher training or when significant changes occur
□ 20.4 Developer training: privacy-by-design, secure coding, data handling
□ 20.5 Confidentiality agreements in place for staff with data access
□ 20.6 Clear data protection policy accessible to all staff
□ 20.7 Escalation path for data protection questions/incidents clear
□ 20.8 GDPR compliance owner identified (DPO or equivalent)

## Section 21 — Technical Documentation [13 pts]

□ 21.1 Data flow diagrams: where data enters, moves, and is stored
□ 21.2 Data inventory: all personal data fields documented with purpose and legal basis
□ 21.3 Architecture diagrams: security zones, encryption points, access controls
□ 21.4 API documentation: which endpoints collect/return PII
□ 21.5 Third-party service list with data sharing details
□ 21.6 Encryption key management documented
□ 21.7 Access control matrix: roles and what data they can access
□ 21.8 Incident response runbook documented and tested
□ 21.9 DSR fulfillment runbook documented and tested
□ 21.10 Backup and recovery procedures documented
□ 21.11 Change management includes privacy impact review
□ 21.12 Security testing results retained
□ 21.13 Vendor security assessments documented

---

## Summary Table

| Section | Pts |
|---------|-----|
| 1. Legal Basis | 20 |
| 2. Consent Management | 18 |
| 3. Privacy Notice | 20 |
| 4. Data Subject Rights | 22 |
| 5. Privacy by Design | 15 |
| 6. Data Security | 18 |
| 7. Data Breach | 12 |
| 8. Processing Register | 10 |
| 9. DPO | 8 |
| 10. Joint Controllers | 6 |
| 11. DPIA | 10 |
| 12. International Transfers | 12 |
| 13. Controller/Processor | 10 |
| 14. Special Categories | 12 |
| 15. Criminal Data | 6 |
| 16. Automated Decisions | 10 |
| 17. Children's Data | 8 |
| 18. Data Retention | 10 |
| 19. Third-Party Integrations & ePrivacy | 10 |
| 20. Staff Training | 8 |
| 21. Technical Documentation | 13 |
| **TOTAL** | **288** |

---

*OpenGDPR v0.5.0 — Last updated 2026-03-17*
