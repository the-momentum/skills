# GDPR Reference Tables v0.5.0

**OpenGDPR by Creativa Legal** — www.creativa.legal | **Tested by Momentum** — www.themomentum.ai

---

## Quick Reference — Key Numbers

| Requirement | Value |
|-------------|-------|
| DSR response deadline | 30 days (+ 60 days extension for complex) |
| Breach notification to supervisory authority | 72 hours (Art. 33) |
| Breach notification to individuals | Without undue delay (Art. 34) |
| Digital consent age (EU default) | 16 years (states may lower to 13) |
| Digital consent age — Poland | 16 years |
| Digital consent age — Germany | 16 years |
| Digital consent age — Spain | 14 years |
| Digital consent age — France | 15 years |
| Digital consent age — Italy | 14 years |
| Processing register retention | As long as processing continues |
| Max fine (higher tier) | €20,000,000 or 4% of global annual turnover |
| Max fine (lower tier) | €10,000,000 or 2% of global annual turnover |
| Encryption at rest (recommendation) | AES-256 |
| TLS minimum | 1.2 (1.3 preferred) |
| Audit log retention | Minimum 5 years (sector-specific may be higher) |
| Data retention period | No longer than necessary (Art. 5(1)(e)) |
| DPIA required before processing | Yes, for high-risk activities (Art. 35) |
| DPO registration | Required in some member states |

---

## Personal Data Categories

| Category | Data Elements | GDPR Basis Needed |
|----------|---------------|-------------------|
| **Identity** | Name, ID document, ID number, passport, driving licence | Art. 6 |
| **Contact** | Email, phone, fax, home address, postal address | Art. 6 |
| **Financial** | IBAN, credit card, transaction history | Art. 6 |
| **Location** | IP address, GPS coordinates, geolocation, cookie ID | Art. 6 |
| **Digital** | User ID, session ID, device fingerprint, MAC, IMEI | Art. 6 |
| **Health** | Diagnosis, medication, blood type, allergies, medical history | Art. 9 — special category |
| **Biometric** | Fingerprint, face scan, iris scan, voice print | Art. 9 — special category |
| **Genetic** | DNA, genetic profile | Art. 9 — special category |
| **Racial/Ethnic** | Race, ethnic origin | Art. 9 — special category |
| **Political** | Political opinions, party membership | Art. 9 — special category |
| **Religious** | Religion, philosophical beliefs | Art. 9 — special category |
| **Trade Union** | Union membership | Art. 9 — special category |
| **Sexual** | Sexual orientation, sex life | Art. 9 — special category |
| **Criminal** | Convictions, offences | Art. 10 — requires specific authorization |
| **Employment** | Job title, employer, CV, employment history | Art. 6 |
| **Education** | Grades, diplomas, education history | Art. 6 |

*This list is illustrative, not exhaustive. Personal data encompasses any information relating to an identified or identifiable natural person (Art. 4(1)).*

**Critical rule**: Data becomes personal data when it allows — directly or indirectly — identification of a natural person (Art. 4(1)). This applies everywhere: databases, APIs, logs, error messages, file names, URLs, code comments.

---

## Legal Bases Comparison (Art. 6 + Art. 9 + Art. 10)

| Basis | Short Name | When Valid | Key Requirements |
|-------|-----------|-----------|-----------------|
| **Art. 6(1)(a)** | Consent | When user genuinely has free choice | Freely given, specific, informed, unambiguous; withdrawable; informed about right to withdraw |
| **Art. 6(1)(b)** | Contract | Processing necessary to fulfil contract | Must be objectively necessary, not just convenient |
| **Art. 6(1)(c)** | Legal obligation | Compliance with EU/member state law | Law must be clear and proportionate |
| **Art. 6(1)(d)** | Vital interests | Life or death situation | Last resort; only when person incapable of consenting |
| **Art. 6(1)(e)** | Public task | Public authority or official authority | Task must be laid down in law |
| **Art. 6(1)(f)** | Legitimate interests | Private entities with genuine interest | LIA required; fundamental rights override |
| **Art. 9(2)(a)** | Consent (Art. 9) | Explicit consent to special category processing | Genuinely explicit consent | Freely given, specific, informed, unambiguous; withdrawable |
| **Art. 9(2)(b)** | Employment | Necessary to fulfill legal obligation | Carrying out obligations and exercising rights of controller or data subject in employment, social security and social protection law |
| **Art. 9(2)(c)** | Vital interests | Subject incapable of giving consent | Protecting vital interests of data subject or natural person |
| **Art. 9(2)(d)** | Legitimate activities | Legitimate activities with appropriate safeguards | Not-for-profit body, members only |
| **Art. 9(2)(e)** | Public | Data made public by subject | Manifestly made public by data subject |
| **Art. 9(2)(f)** | Legal claims | Establishment, exercise or defence of legal claims | Including courts in judicial capacity |
| **Art. 9(2)(g)** | Public interest | Substantial public interest | Based on EU/Member State law, proportionate to objective |
| **Art. 9(2)(h)** | Preventive/occupational medicine | Preventive or occupational medicine | Assessment of working capacity, medical diagnosis, health/social care; under professional secrecy |
| **Art. 9(2)(i)** | Public health | Public interest in public health | Cross-border threats to health, quality/safety standards for healthcare/medicines |
| **Art. 9(2)(j)** | Scientific/research | Public interest, research, statistics | Archiving, scientific/historical research, statistics; Art. 89(1) safeguards |
| **Art. 10** | Official authority (criminal) | Data relating to criminal convictions/offences | Control of official authority or authorized by EU/state law |

---

## Consent Requirements Checklist (Art. 7)

| Requirement | Description |
|-------------|-------------|
| **Freely given** | No power imbalance; no conditioning service on non-necessary consent |
| **Specific** | For a specific, clearly defined purpose |
| **Informed** | Data subject understands what they're consenting to |
| **Unambiguous** | Clear affirmative action (no pre-ticked boxes, no silence/inactivity) |
| **Granular** | Separate consent for separate purposes |
| **Withdrawable** | As easy to withdraw as to give |
| **Informed about withdrawal** | Informed about right to withdraw at any time |
| **Documented** | Timestamp, version of consent text, mechanism used |
| **Age-appropriate** | Parental consent for under-16 (or lower member state threshold) |

---

## DPIA Triggers (Art. 35)

DPIA **required** when processing is likely to result in high risk. Supervisory authorities have published lists. Key triggers:

| Trigger | Examples |
|---------|---------|
| Systematic evaluation of personal aspects (profiling) | Credit scoring, behavioral advertising, HR decisions, insurance risk |
| Large-scale processing of special categories (Art. 9/10) | Health apps, genetic testing, criminal records |
| Systematic monitoring of publicly accessible areas | CCTV, location tracking, Wi-Fi tracking |
| Large-scale processing of data concerning vulnerable subjects | Children, elderly, patients |
| Innovative technology | AI/ML, biometrics, IoT |
| Preventing individuals from exercising their rights | Blacklists, fraud detection with serious consequences |
| Transferring personal data to countries without adequate protection | Without appropriate safeguards |
| Matching/combining datasets | Unexpected secondary uses from combined data |

---

## International Transfer Mechanisms (Art. 44-49)

| Mechanism | Description | Status (2026) |
|-----------|-------------|---------------|
| **Adequacy decision** (Art. 45) | Country deemed adequate by EC | UK, Japan, South Korea, Canada (commercial), Switzerland, Israel, New Zealand, Andorra, Argentina, Brazil, Uruguay, others |
| **SCCs** (Art. 46(2)(c)) | Standard Contractual Clauses | 2021 version required |
| **BCRs** (Art. 47) | Binding Corporate Rules for group transfers | Approved by supervisory authority |
| **EU-US DPF** | EU-US Data Privacy Framework | Valid since July 2023 (Schrems III risk: monitor) |
| **Code of conduct** (Art. 40) | Industry-approved code | Limited adoption |
| **Certification** (Art. 42) | Approved certification mechanism | Limited adoption |
| **Derogations** (Art. 49) | Last resort: explicit consent, contract necessity, public interest | Only occasional use |

---

## Supervisory Authorities — Key Contacts

| Country | Authority | Website |
|---------|-----------|---------|
| Poland | UODO (Urząd Ochrony Danych Osobowych) | uodo.gov.pl |
| Germany | BfDI + state-level DPAs | bfdi.bund.de |
| France | CNIL | cnil.fr |
| Italy | Garante | garanteprivacy.it |
| Spain | AEPD | aepd.es |
| Netherlands | AP (Autoriteit Persoonsgegevens) | autoriteitpersoonsgegevens.nl |
| Ireland | DPC (Data Protection Commission) | dataprotection.ie |
| EU-wide guidance | EDPB (European Data Protection Board) | edpb.europa.eu |

---

## Penalty Tiers

| Tier | Max Amount | Violations |
|------|-----------|------------|
| **Higher** | €20M or 4% global turnover | Art. 5, 6, 7, 9, 12-22, 44-49, 58(2) |
| **Lower** | €10M or 2% global turnover | Art. 8, 11, 25-39, 41(4), 42-43 |

Most cited violations in enforcement: (1) insufficient legal basis, (2) lack of consent/invalid consent, (3) data subjects' rights violations, (4) insufficient security, (5) data transfers without safeguards.

---

## Retention Guidelines by Data Type

| Data Type | Typical Retention | Legal Basis |
|-----------|-------------------|-------------|
| Account data (active users) | Duration of account + grace period | Contract |
| Account data (deleted users) | 30-90 days after deletion request | Legal obligation / consent |
| Financial/billing records | 5-10 years | Tax/accounting law (varies by country) |
| Medical records | 10-30 years | Health sector law |
| Employee data (post-employment) | 2-5 years | Employment law |
| Access/audit logs | 1-5 years | Legitimate interest / legal obligation |
| Marketing consent records | Life of consent + 3 years | Art. 7 (demonstrate compliance) |
| CCTV footage | 30-72 hours (or 30 days if needed) | Legitimate interest |
| Cookies (functional) | Session or up to 12 months | Strict necessity |
| Cookies (analytics/marketing) | Up to 12 months | Consent |

*Always verify against applicable sector regulations and member state law.*

---

## ePrivacy & Cookies (Directive 2002/58/EC)

Cookie and tracking compliance is governed by both GDPR and the **ePrivacy Directive (2002/58/EC)**, specifically:

- **Recital 30** — Prior consent requirement for cookies and tracking
- **Art. 5-7** — General electronic commerce rules, confidentiality
- **Art. 13-14** — Unsolicited marketing communications; Do Not Call registers

**Key alignment**:
- Consent under GDPR Art. 7 must also satisfy ePrivacy requirements
- "Strictly necessary" cookies (functional) may be exempt from consent under both frameworks
- Analytics and marketing cookies require explicit consent before deployment
- Withdrawal of GDPR consent is equivalent to revoking ePrivacy consent

---

*OpenGDPR v0.5.0 — Last updated 2026-03-17*
