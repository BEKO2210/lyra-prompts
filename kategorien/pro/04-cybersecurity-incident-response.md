---
titel: "Cybersecurity Incident Response & Forensic Analysis"
kategorie: "Pro"
unterkategorie: "IT-Sicherheit & Incident Response"
tags: ["Cybersecurity", "Incident Response", "Forensik", "Threat Hunting", "CoT", "ToT", "Reflection"]
erstellt: "2026-02-21"
plattformen: ["Claude", "GPT-4", "Kimi", "Gemini"]
autor: "LYRA Prompt Engineering"
version: "1.0.0"
---

# Cybersecurity Incident Response & Forensic Analysis

## Prompt

```
Du bist ein Senior Incident Response Lead (GCIH, GCFA) mit 15+ Jahren 
Erfahrung in Enterprise-Security. Führe eine strukturierte Incident 
Response und Forensic Analysis durch.

**INCIDENT-KONTEXT:**
Erkennungsmethode: [SIEM-ALERT/USER-REPORT/THREAT-INTEL/ANDERE]
Initialer Indikator: [BESCHREIBE DEN AUSLÖSER]
Betroffene Systeme: [SYSTEME/NETZWERKSEGMENTE]
Zeitpunkt der Erkennung: [DATUM/ZEIT]
Organisationskontext: [BRANCHE/GRÖßE/COMPLIANCE-ANFORDERUNGEN]

**DEINE AUFGABE:**
Führe eine vollständige Incident Response durch Multi-Layer-Reasoning.

**CHAIN-OF-THOUGHT ANWEISUNG:**

[SCHRITT 1: INITIALE BEWERTUNG & TRIAGE]
Explizite Analyse der Situation:
- Einordnung nach NIST SP 800-61 Phasen
- Initialer Schweregrad (P1-Critical bis P4-Low)
- Betroffene CIA-Trias (Confidentiality/Integrity/Availability)
- Potenzielle Auswirkungen (Business Impact Assessment)
- Sofortige Containment-Notwendigkeit (Ja/Nein + Begründung)
- Eskalationspfad (wer muss informiert werden?)

[SCHRITT 2: EVIDENCE ACQUISITION PLAN]
Entwickle einen forensischen Erwerbungsplan:
- Volatile Daten (RAM, Netzwerk-Verbindungen, Prozesse)
- Non-volatile Daten (Festplatten, Logs, Backups)
- Netzwerk-Evidence (PCAPs, Firewall-Logs, Proxy-Logs)
- Cloud-Evidence (CloudTrail, Azure AD Logs, SaaS-Logs)
- Chain of Custody Dokumentation
- Imaging-Strategie (dd, FTK, Velociraptor, etc.)
- Priorisierung (was zuerst, warum?)

[SCHRITT 3: TREE-OF-THOUGHTS: THREAT SCENARIOS]
Exploriere 3 alternative Bedrohungsszenarien:

PFAD A: Ransomware-Angriff
- Initial Access: Phishing oder RDP-Exploit
- Lateral Movement: PSExec, WMI, RDP-Hopping
- Data Exfiltration: Vor Verschlüsselung
- Impact: Verschlüsselung + Doppelterpressung
→ IOCs: Datei-Erweiterungen, Ransom-Notes, TOR-Verbindungen
→ Response: Isolation, Backup-Restore, keine Zahlung

PFAD B: APT/Data Exfiltration
- Initial Access: Supply Chain oder Spear Phishing
- Persistence: Golden SAML, Domain Controller Compromise
- Collection: Langsame, selektive Daten-Extraktion
- Impact: IP-Diebstahl, Regulatorische Konsequenzen
→ IOCs: C2-Kommunikation, ungewöhnliche Daten-Transfers
→ Response: Langfristige Containment, Threat Hunting

PFAD C: Insider Threat / Sabotage
- Access: Legitime Credentials, physikalischer Zugang
- Actions: Datenlöschung, System-Manipulation
- Motivation: Finanziell, Rache, Ideologisch
- Impact: Datenverlust, Betriebsunterbrechung
→ IOCs: Ungewöhnliche Zugriffszeiten, Bulk-Deletes
→ Response: HR/Legal involvieren, forensische Analyse

Für jeden Pfad:
- Wahrscheinlichkeit einschätzen (Hoch/Mittel/Niedrig)
- Passende IOCs identifizieren
- Spezifische Response-Aktionen definieren
- Evidence-Sources priorisieren

[SCHRITT 4: FORENSIC ANALYSIS WORKFLOW]
Für das wahrscheinlichste Szenario, detailliere:

a) Timeline-Rekonstruktion:
   - First Known Bad (FKB)
   - Initial Access Vector
   - Persistence-Mechanismen
   - Lateral Movement-Pfade
   - Actions on Objective
   - Erkennungszeitpunkt

b) Log-Analyse:
   - Windows Event Logs (Security, System, PowerShell)
   - Network Logs (Firewall, IDS/IPS, DNS)
   - Authentication Logs (AD, VPN, Cloud)
   - Endpoint Logs (EDR, Sysmon)
   - Korrelation und Pivoting

c) Malware-Analyse (falls zutreffend):
   - Static Analysis (Strings, Hashes, Imports)
   - Dynamic Analysis (Sandbox-Verhalten)
   - Memory Analysis (Volatility, Rekall)
   - C2-Extraktion und Decoding

d) Memory Forensics:
   - Volatile Artifacts (Processes, Network, DLLs)
   - Malware in Memory
   - Credential Dumping-Spuren
   - Anti-Forensics-Indikatoren

[SCHRITT 5: SELF-CONSISTENCY CHECK]
Validiere deine Analyse:

□ Timeline-Konsistenz: Passen alle Events logisch zusammen?
□ IOC-Verifizierung: Sind alle IOCs validiert (nicht nur vermutet)?
□ Scope-Validation: Ist die Betroffenheit vollständig ermittelt?
□ False-Positive-Check: Könnten legitime Aktivitäten vorliegen?
□ Attribution-Certainty: Wie sicher ist die Zuordnung?

Prüfe auf Analyse-Fehler:
□ Confirmation Bias: Werden nur bestätigende Daten betrachtet?
□ Anchoring: Ist die erste Hypothese zu stark gewichtet?
□ Availability Heuristic: Sind seltene, aber wichtige Indikatoren 
   übersehen?
□ Premature Closure: Wurden alle Szenarien ausreichend geprüft?

[SCHRITT 6: CONTAINMENT, ERADICATION & RECOVERY]
Entwickle den Response-Plan:

Containment (Short-term):
- Sofortmaßnahmen (Isolation, Account-Disable)
- Segmentierung (VLAN, Firewall-Rules)
- Evidence Preservation

Containment (Long-term):
- Patch-Management
- Credential Reset-Strategie
- Security Control-Hardening

Eradication:
- Malware-Entfernung
- Backdoor-Eliminierung
- Persistence-Removal

Recovery:
- System-Wiederherstellung (Priorisierung)
- Daten-Restore (aus sauberen Backups)
- Monitoring-Verstärkung
- Business-Continuity-Tests

[SCHRITT 7: REFLECTION & LESSONS LEARNED]
Selbstkritische Analyse:

- Was wurde übersehen bei der initialen Bewertung?
- Welche Annahmen haben sich als falsch erwiesen?
- Wie hätte die Erkennung früher erfolgen können?
- Was funktionierte gut im Response?
- Was muss im Incident Response Plan verbessert werden?

Post-Incident Aktivitäten:
- Indicators of Compromise (IOCs) für Threat Intel
- Detection-Rule-Verbesserungen
- Security-Awareness-Training-Bedarf
- Technische Control-Gaps
- Prozess-Verbesserungen

**AUSGABEFORMAT:**

## Incident Summary
[Executive Summary für Management - 1 Seite]

## Initial Assessment
[Triage-Ergebnisse, Schweregrad, Impact]

## Threat Scenario Analysis
[Vergleich der 3 Pfade mit Empfehlung]

## Forensic Findings
[Timeline, IOCs, Malware-Analyse, Log-Ergebnisse]

## Scope of Compromise
[Betroffene Systeme, Daten, Accounts]

## Response Actions Taken
[Containment, Eradication, Recovery]

## IOC List
[Hashs, IPs, Domains, Filepaths, Registry-Keys]

## Recommendations
[Kurz-, Mittel-, Langfristige Maßnahmen]

## Lessons Learned
[Was wurde gelernt, was ändern wir?]
```

## Chain-of-Thought Struktur

```
┌─────────────────────────────────────────────────────────────────────┐
│           CYBERSECURITY INCIDENT RESPONSE REASONING                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  [LAYER 1: INITIAL TRIAGE]                                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │   NIST      │  │  Severity   │  │   CIA       │  │  Business   │ │
│  │   Phase     │  │ Assessment  │  │   Impact    │  │   Impact    │ │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘ │
│         └─────────────────┴─────────────────┴─────────────────┘      │
│                              │                                       │
│                              ▼                                       │
│  [LAYER 2: EVIDENCE ACQUISITION]                                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │   Volatile  │  │ Non-Volatile│  │   Network   │  │    Cloud    │ │
│  │    Data     │  │    Data     │  │   Evidence  │  │  Evidence   │ │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘ │
│         └─────────────────┴─────────────────┴─────────────────┘      │
│                              │                                       │
│                              ▼                                       │
│  [LAYER 3: TREE-OF-THOUGHTS]                                         │
│              ┌───────────────────────────────────────┐              │
│              │         THREAT SCENARIO TREE           │              │
│              │                   │                    │              │
│         ┌────┴────┐         ┌────┴────┐         ┌────┴────┐        │
│         │  PFAD A │         │  PFAD B │         │  PFAD C │        │
│         │Ransomware│         │   APT   │         │ Insider │        │
│         │         │         │         │         │ Threat  │        │
│         │         │         │         │         │         │        │
│         │• Phishing│         │• Supply │         │• Legit. │        │
│         │• RDP    │         │  Chain  │         │  Access │        │
│         │• Encrypt│         │• C2 Com.│         │• Sabotage│       │
│         └────┬────┘         └────┬────┘         └────┬────┘        │
│              └───────────────────┼───────────────────┘              │
│                                  │                                  │
│                    ┌─────────────┴─────────────┐                   │
│                    │   EVIDENCE PRIORITIZATION  │                   │
│                    │  (Likelihood × Impact)     │                   │
│                    └─────────────┬─────────────┘                   │
│                                  │                                  │
│                                  ▼                                  │
│  [LAYER 4: FORENSIC ANALYSIS]                                        │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │   Timeline    │    Logs     │   Malware   │    Memory       │   │
│  │Reconstruction │  Analysis   │  Analysis   │   Forensics     │   │
│  │  • FKB        │  • Windows  │  • Static   │  • Volatile     │   │
│  │  • Access     │  • Network  │  • Dynamic  │  • Processes    │   │
│  │  • Movement   │  • Auth     │  • Memory   │  • Credentials  │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                  │                                  │
│                                  ▼                                  │
│  [LAYER 5: VALIDATION]                                               │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    ANALYSIS VALIDATION                       │   │
│  │  □ Timeline Consistency  □ IOC Verification                  │   │
│  │  □ Scope Validation      □ False-Positive Check              │   │
│  │  □ No Confirmation Bias  □ No Premature Closure              │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                  │                                  │
│                                  ▼                                  │
│  [LAYER 6: RESPONSE]                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌────────────┐ │
│  │  Short-Term │  │  Long-Term  │  │Eradication │  │  Recovery  │ │
│  │  Containment│  │  Containment│  │            │  │            │ │
│  │  (Isolate)  │  │  (Segment)  │  │  (Remove)  │  │  (Restore) │ │
│  └─────────────┘  └─────────────┘  └─────────────┘  └────────────┘ │
│                                  │                                  │
│                                  ▼                                  │
│  [LAYER 7: REFLECTION]                                               │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌────────────┐ │
│  │   Missed    │  │  Wrong      │  │  Detection  │  │   IR Plan  │ │
│  │   Signals   │  │  Assumptions│  │  Gaps       │  │  Improve.  │ │
│  └─────────────┘  └─────────────┘  └─────────────┘  └────────────┘ │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

## Anwendung mit komplexem Beispiel

### Szenario: Verdacht auf APT in Finanzdienstleister

**Input:**
```
Erkennungsmethode: SIEM-Alert (unusual data transfer)
Initialer Indikator: 2TB Daten-Upload zu unbekannter IP über 3 Tage
Betroffene Systeme: Fileserver FIN-FS-01, Workstation FIN-WS-42
Zeitpunkt: 2026-02-15 03:47 UTC
Organisation: Mittelständische Bank, 500 Mitarbeiter, BSI-Grundschutz
```

**Erwartete CoT-Ausgabe:**

### Schritt 3: Tree-of-Thoughts Exploration

```
PFAD A: RANSOMWARE (Wahrscheinlichkeit: NIEDRIG)
┌─────────────────────────────────────────────────────────────┐
│ Argumente dagegen:                                          │
│ • Keine Verschlüsselung beobachtet                          │
│ • Keine Ransom-Notes gefunden                               │
│ • Daten-Exfiltration vor Verschlüsselung untypisch          │
│                                                             │
│ Argumente dafür:                                            │
│ • Double-Extortion-Taktik möglich                           │
│ • "Steal-then-Encrypt" Muster bei modernen Ransomware       │
│                                                             │
│ Einschätzung: 20% Wahrscheinlichkeit                        │
│ → Trotzdem IOCs für Ransomware prüfen                       │
└─────────────────────────────────────────────────────────────┘

PFAD B: APT / DATA EXFILTRATION (Wahrscheinlichkeit: HOCH)
┌─────────────────────────────────────────────────────────────┐
│ Argumente dafür:                                            │
│ • Große Datenmenge über längeren Zeitraum                   │
│ • Ungewöhnliche Ziel-IP (nicht in Threat-Intel)             │
│ • Zeitpunkt (3:47 UTC = außerhalb Geschäftszeiten)          │
│ • Nur 2 Systeme betroffen (gezielte Auswahl?)               │
│                                                             │
│ APT-Gruppen-Verdacht:                                       │
│ • FIN7, Carbanak, oder ähnliche Finanz-APT                  │
│ • Möglicherweise Initial Access über Phishing               │
│                                                             │
│ Einschätzung: 70% Wahrscheinlichkeit                        │
│ → Hauptfokus der Untersuchung                               │
└─────────────────────────────────────────────────────────────┘

PFAD C: INSIDER THREAT (Wahrscheinlichkeit: MITTEL)
┌─────────────────────────────────────────────────────────────┐
│ Argumente dafür:                                            │
│ • FIN-WS-42 gehört zu Mitarbeiter in Kündigungsfrist        │
│ • Zugriff auf sensible Daten erklärbar                      │
│ • Upload während Nachtschicht (unüblich für diesen MA)      │
│                                                             │
│ Argumente dagegen:                                          │
│ • 2TB über normale Workstation ungewöhnlich                 │
│ • Technische Sophistication (verschlüsselter Upload)        │
│                                                             │
│ Einschätzung: 30% Wahrscheinlichkeit                        │
│ → HR/Legal parallel involvieren                             │
└─────────────────────────────────────────────────────────────┘

EMPFIEHLUNG: Primär PFAD B (APT) untersuchen, PFAD C nicht ausschließen
```

### Schritt 4: Forensic Analysis Workflow

```
TIMELINE-REKONSTRUKTION:
┌─────────────────────────────────────────────────────────────┐
│ 2026-02-10 14:23 │ Phishing-Email empfangen (FIN-WS-42)     │
│                  │ Subject: "Q4 Finanzbericht - Dringend"    │
│                  │ Attachment: Q4_Report.xlsm (Macro)        │
│                                                             │
│ 2026-02-10 14:31 │ Macro aktiviert, Cobalt Strike Beacon     │
│                  │ C2: 185.220.101[.]47:443                  │
│                                                             │
│ 2026-02-10 15:45 │ Lateral Movement zu FIN-FS-01 via         │
│                  │ Pass-the-Hash (Domain Admin Credentials)  │
│                                                             │
│ 2026-02-12 02:15 │ Data Staging beginnt (FIN-FS-01)          │
│                  │ 50GB Archive erstellt in C:\Windows\Temp  │
│                                                             │
│ 2026-02-15 03:47 │ Data Exfiltration beginnt (SIEM Alert)    │
│                  │ Upload zu 91.243.44[.]201:8080            │
│                                                             │
│ 2026-02-15 06:12 │ Erkennung durch SOC, Incident Response    │
│                  │ initialisiert                             │
└─────────────────────────────────────────────────────────────┘

LOG-ANALYSE ERGEBNISSE:
┌─────────────────────────────────────────────────────────────┐
│ Windows Security Logs (FIN-WS-42):                          │
│ • Event ID 4624: Anmeldung mit kompromittierten Credentials │
│ • Event ID 4648: Explizite Credential-Verwendung            │
│ • Event ID 4672: Admin-Rechte verwendet                     │
│                                                             │
│ Network Logs (Firewall):                                    │
│ • Verbindungen zu 185.220.101[.]47:443 (C2)                 │
│ • Verbindungen zu 91.243.44[.]201:8080 (Exfiltration)       │
│ • DNS-Queries zu DGA-Domains (ca. 50 unique)                │
│                                                             │
│ Proxy Logs:                                                 │
│ • Keine direkten Downloads (vermutlich über C2)             │
│ • Ungewöhnliche User-Agent Strings                          │
└─────────────────────────────────────────────────────────────┘

MALWARE-ANALYSE:
┌─────────────────────────────────────────────────────────────┐
│ Q4_Report.xlsm:                                             │
│ • SHA256: a3f5c8... (bekanntes Cobalt Strike Stager)        │
│ • VBA-Macro lädt Payload von Pastebin-ähnlichem Service     │
│ • Detection: 45/70 auf VirusTotal                           │
│                                                             │
│ Cobalt Strike Beacon (Memory):                              │
│ • Config extrahiert: C2-Server, Jitter, User-Agent          │
│ • Malleable C2-Profile: "amazon.profile" (Tarnung)          │
│ • Noch aktive Sessions in anderen Systemen vermutet         │
└─────────────────────────────────────────────────────────────┘
```

### Schritt 5: Self-Consistency Check

```
VALIDIERUNG:

Timeline-Konsistenz: ✓ PASS
• Alle Events chronologisch logisch
• Zeitfenster zwischen Events plausibel für APT-Taktik

IOC-Verifizierung: ✓ PASS
• C2-IP in Threat-Intel (Recorded Future: APT29-verdächtig)
• File-Hash in VirusTotal bestätigt
• DGA-Pattern mit APT29-Malware übereinstimmend

Scope-Validation: ⚠️ PARTIAL
• FIN-FS-01 und FIN-WS-42 bestätigt kompromittiert
• Domain Controller: Noch keine Anzeichen, aber nicht ausgeschlossen
• Weitere Systeme: Untersuchung läuft

False-Positive-Check: ✓ PASS
• Data-Transfer-Volumen eindeutig anomal
• C2-Kommunikation unbestreitbar
• Keine legitime Business-Justification

Attribution-Certainty: ⚠️ MEDIUM
• TTPs passen zu APT29 (Cozy Bear)
• C2-Infrastruktur shared mit anderen APTs
• Keine eindeutigen Attribution-Indikatoren
```

## Variationen für verschiedene Komplexitätsstufen

### Level 1: Foundation (Triage)
```
Bewerte folgenden Security-Alert: [ALERT-DETAILS]

1. Schweregrad einstufen (P1-P4)
2. Wahrscheinlichstes Szenario identifizieren
3. Sofortmaßnahmen definieren

Ausgabe: 1-seitige Triage-Bewertung
```

### Level 2: Professional (Standard)
```
[Standard-Prompt wie oben]

Zusätzlich:
- Evidence-Acquisition-Plan
- Timeline-Rekonstruktion
- Containment-Strategie
```

### Level 3: Elite (Full Prompt)
```
[Vollständiger Prompt mit allen 7 Schritten]

Zusätzliche Anforderungen:
- Detaillierte Malware-Analyse
- Memory-Forensics-Workflow
- Threat-Intelligence-Integration
- Recovery-Plan mit Priorisierung
- Kommunikations-Plan (intern/extern/Regulatoren)
```

### Level 4: Masterclass (Enterprise Incident)
```
[Elite-Level] +

Erweiterungen:
- Multi-Site Incident Koordination
- Supply-Chain-Compromise-Untersuchung
- Attribution-Analyse (Nation State Actor)
- Regulatory Notification-Strategie (GDPR, SEC, etc.)
- Crisis Communication (Media, Customers)
- Legal Hold und eDiscovery
- Cyber-Insurance-Koordination
- Post-Incident Threat Hunting
```

## Prompt-Metadaten

| Attribut | Wert |
|----------|------|
| Komplexität | ★★★★★ |
| Token-Schätzung | 4.000-8.000 |
| Ausführungszeit | 20-45 Minuten |
| Domäne | Cybersecurity / Incident Response |
| Beste Modelle | Claude 3.5 Sonnet, GPT-4, Kimi K2.5 |

## Erfolgskriterien

- [ ] Alle 7 Denkschritte explizit durchlaufen
- [ ] Mindestens 3 Threat-Szenarien exploriert
- [ ] Timeline logisch konsistent
- [ ] IOCs verifiziert, nicht nur vermutet
- [ ] Cognitive Biases explizit geprüft
- [ ] Scope of Compromise vollständig ermittelt
- [ ] Lessons Learned dokumentiert
