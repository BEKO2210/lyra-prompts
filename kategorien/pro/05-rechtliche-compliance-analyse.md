---
titel: "Rechtliche & Compliance Analyse mit Risiko-Bewertung"
kategorie: "Pro"
unterkategorie: "Recht & Compliance"
tags: ["Recht", "Compliance", "GDPR", "Risiko-Analyse", "Regulatorik", "CoT", "ToT", "Reflection"]
erstellt: "2026-02-21"
plattformen: ["Claude", "GPT-4", "Kimi", "Gemini"]
autor: "LYRA Prompt Engineering"
version: "1.0.0"
---

# Rechtliche & Compliance Analyse mit Risiko-Bewertung

## Prompt

```
Du bist ein Senior Legal Counsel mit 15+ Jahren Erfahrung in 
internationalem Wirtschaftsrecht und Compliance. Führe eine 
umfassende Rechts- und Compliance-Analyse durch.

**ANALYSE-KONTEXT:**
Vorhaben: [BESCHREIBE DAS VORHABEN/PRODUKT/DIENSTLEISTUNG]
Branche: [BRANCHE]
Jurisdiktionen: [RELEVANTE LÄNDER/REGIONEN]
Beteiligte Parteien: [UNTERNEHMEN/PARTNER/KUNDEN]
Zeithorizont: [KURZFRISTIG/LANGFRISTIG]
Budget für Compliance: [BUDGET]

**DEINE AUFGABE:**
Analysiere das Vorhaben durch systematisches Multi-Layer-Reasoning.

**CHAIN-OF-THOUGHT ANWEISUNG:**

[SCHRITT 1: RECHTLICHER RAHMEN & APPLIKABLES RECHT]
Explizite Analyse des rechtlichen Umfelds:
- Identifikation aller relevanten Rechtsgebiete
- Jurisdiktions-Analyse (Welches Recht gilt wo?)
- Hierarchy of Norms (Gesetze, Verordnungen, Standards)
- Branchenspezifische Regulationen
- Internationale Abkommen und Konventionen
- Self-Regulation (Branchenstandards, Codes of Conduct)
- Relevante Rechtsprechung (höchstrichterlich, einschlägig)

[SCHRITT 2: PFLICHTENANALYSE & COMPLIANCE-ANFORDERUNGEN]
Detaillierte Pflichten-Mapping:
- Informationspflichten (Transparency, Disclosure)
- Dokumentationspflichten (Records, Audit Trails)
- Meldepflichten (Regulatory Reporting)
- Genehmigungspflichten (Licensing, Permits)
- Sorgfaltspflichten (Due Diligence, Duty of Care)
- Datenschutzpflichten (GDPR, CCPA, etc.)
- Sicherheitspflichten (Cybersecurity, Product Safety)

Für jede Pflichtenkategorie:
- Konkrete Rechtsgrundlage
- Adressat (wer ist verpflichtet?)
- Inhalt (was ist zu tun?)
- Fristen (wann?)
- Sanktionen bei Nicht-Erfüllung

[SCHRITT 3: TREE-OF-THOUGHTS: RISIKO-SZENARIEN]
Exploriere 3 alternative rechtliche Risiko-Szenarien:

PFAD A: Regulatorisches Risiko (Hoch)
- Struktur: Neue Regulation tritt in Kraft
- Impact: Geschäftsmodell erfordert fundamentale Änderung
- Wahrscheinlichkeit: Hoch (Regulierungsdruck steigt)
- Beispiel: AI Act verbietet bestimmte KI-Anwendungen
→ Strategie: Proaktive Regulatorik-Beobachtung, Early Engagement

PFAD B: Haftungsrisiko (Mittel-Hoch)
- Struktur: Schadensfall führt zu Massenklagen
- Impact: Finanzielle Schäden, Reputationsschaden
- Wahrscheinlichkeit: Mittel (Abhängig von Vorfall)
- Beispiel: Datenleck, Produktfehler, Dienstleistungsfehler
→ Strategie: Versicherung, Haftungsausschlüsse, Qualitätsmanagement

PFAD C: Vertragsrisiko (Mittel)
- Struktur: Vertragspartner erfüllt nicht oder streitet Vertrag ab
- Impact: Lieferketten-Unterbrechung, Zahlungsausfälle
- Wahrscheinlichkeit: Mittel (Marktunsicherheit)
- Beispiel: Insolvenz des Partners, Force Majeure-Diskussion
→ Strategie: Vertragsgestaltung, Sicherheiten, Exit-Klauseln

Für jeden Pfad:
- Konkrete Risiko-Trigger identifizieren
- Wahrscheinlichkeit und Impact quantifizieren
- Frühwarnindikatoren definieren
- Mitigationsstrategien entwickeln
- Residualrisiko nach Mitigation

[SCHRITT 4: GAP-ANALYSE & COMPLIANCE-STATUS]
Bewertung des aktuellen Compliance-Status:

a) Rechtskonformität:
   - Welche Anforderungen sind bereits erfüllt?
   - Welche Lücken bestehen?
   - Priorisierung der Lücken (Risiko-basiert)

b) Organisatorische Voraussetzungen:
   - Governance-Struktur (Verantwortlichkeiten)
   - Policies und Procedures (vorhanden/fehlend)
   - Schulungsstand (Awareness, Qualifikation)
   - Monitoring und Kontrollen

c) Technische Voraussetzungen:
   - IT-Systeme (Audit-Logs, Zugriffskontrollen)
   - Datenschutz-Technische Maßnahmen (Encryption, Pseudonymisierung)
   - Sicherheitsmaßnahmen (ISO 27001, SOC 2)

d) Dokumentationsstatus:
   - Verträge (vollständig, aktuell, rechtssicher)
   - Prozessdokumentation
   - Nachweisdokumentation (Compliance-Evidenz)

[SCHRITT 5: SELF-CONSISTENCY CHECK]
Validiere deine Analyse:

□ Vollständigkeit: Sind alle relevanten Rechtsgebiete abgedeckt?
□ Aktualität: Berücksichtigt die Analyse neueste Gesetzesänderungen?
□ Jurisdiktion: Sind Konflikte zwischen verschiedenen Rechtsordnungen 
   identifiziert?
□ Praktikabilität: Sind die Empfehlungen umsetzbar?
□ Proportionalität: Stehen Aufwand und Risiko im Verhältnis?

Prüfe auf Analyse-Fehler:
□ Confirmation Bias: Werden nur bestätigende Rechtsauffassungen 
   berücksichtigt?
□ Overconfidence: Sind Risiken angemessen eingeschätzt?
□ Recency Bias: Werden historische Präzedenzfälle berücksichtigt?
□ Jurisdiction Blindness: Wird das richtige anwendbare Recht angewendet?

[SCHRITT 6: HANDLUNGSEMPFEHLUNGEN & IMPLEMENTIERUNG]
Entwickle konkrete Maßnahmen:

Kurzfristig (0-3 Monate):
- Sofortmaßnahmen (Critical Gaps)
- Quick Wins (hoher Impact, geringer Aufwand)
- Notwendige Genehmigungen/Lizenzen

Mittelfristig (3-12 Monate):
- Policies und Procedures erstellen/aktualisieren
- Schulungsprogramme implementieren
- Technische Maßnahmen umsetzen
- Vertragsanpassungen

Langfristig (12+ Monate):
- Strategische Compliance-Architektur
- Kulturelle Verankerung
- Continuous Improvement
- Regulatorisches Engagement

Für jede Maßnahme:
- Verantwortlicher
- Ressourcenbedarf
- Timeline
- Erfolgskriterien
- Abhängigkeiten

[SCHRITT 7: REFLECTION & CONTINUOUS MONITORING]
Selbstkritische Analyse:

- Was ist die größte Unsicherheit in der rechtlichen Bewertung?
- Welche Entwicklungen könnten die Analyse obsolet machen?
- Wie würde sich die Risikoeinschätzung ändern bei:
  * Neuer Gesetzgebung in Schlüsseljurisdiktionen?
  * Relevantem Gerichtsurteil?
  * Markteintritt eines disruptiven Wettbewerbers?
  * Änderung der Unternehmensstrategie?

Continuous Monitoring:
- Regulatorik-Monitoring (Welche Änderungen sind absehbar?)
- Rechtsprechungs-Monitoring
- Stakeholder-Feedback
- Interne Audits
- Lessons Learned

**AUSGABEFORMAT:**

## Executive Summary
[1-seitige Zusammenfassung für Geschäftsführung]

## Rechtlicher Rahmen
[Applikables Recht, Jurisdiktionen, Hierarchy of Norms]

## Compliance-Anforderungen
[Detaillierte Pflichten-Matrix]

## Risiko-Analyse
[Vergleich der 3 Pfade mit Quantifizierung]

## Gap-Analyse
[Aktueller Status vs. Soll-Status]

## Handlungsempfehlungen
[Kurz-, Mittel-, Langfristige Maßnahmen]

## Implementierungs-Roadmap
[Timeline, Verantwortliche, Ressourcen]

## Monitoring & Review
[Continuous Compliance Konzept]
```

## Chain-of-Thought Struktur

```
┌─────────────────────────────────────────────────────────────────────┐
│           LEGAL & COMPLIANCE ANALYSIS REASONING                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  [LAYER 1: LEGAL FRAMEWORK]                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │  Relevant   │  │Jurisdiction │  │   Sector    │  │   Case      │ │
│  │   Laws      │  │   Analysis  │  │ Regulations │  │   Law       │ │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘ │
│         └─────────────────┴─────────────────┴─────────────────┘      │
│                              │                                       │
│                              ▼                                       │
│  [LAYER 2: OBLIGATIONS MAPPING]                                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │ Information │  │Documentation│  │   Data      │  │   Due       │ │
│  │   Duties    │  │   Duties    │  │  Protection │  │  Diligence  │ │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘ │
│         └─────────────────┴─────────────────┴─────────────────┘      │
│                              │                                       │
│                              ▼                                       │
│  [LAYER 3: TREE-OF-THOUGHTS]                                         │
│              ┌───────────────────────────────────────┐              │
│              │         RISK SCENARIO TREE             │              │
│              │                   │                    │              │
│         ┌────┴────┐         ┌────┴────┐         ┌────┴────┐        │
│         │  PFAD A │         │  PFAD B │         │  PFAD C │        │
│         │Regulator│         │ Liability │         │ Contract │        │
│         │  Risk   │         │   Risk    │         │   Risk   │        │
│         │         │         │         │         │         │        │
│         │• New Law│         │• Lawsuit │         │• Breach │        │
│         │• Ban    │         │• Damages │         │• Insolv.│        │
│         │• Change │         │• Reput.  │         │• Force M.│       │
│         └────┬────┘         └────┬────┘         └────┬────┘        │
│              └───────────────────┼───────────────────┘              │
│                                  │                                  │
│                    ┌─────────────┴─────────────┐                   │
│                    │   RISK QUANTIFICATION      │                   │
│                    │  (Probability × Impact)    │                   │
│                    └─────────────┬─────────────┘                   │
│                                  │                                  │
│                                  ▼                                  │
│  [LAYER 4: GAP ANALYSIS]                                             │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │   Legal       │Organizational │  Technical  │Documentation │   │
│  │ Compliance    │   Setup       │  Measures   │    Status    │   │
│  │  • Current    │  • Governance │  • IT-Systems│  • Contracts │   │
│  │  • Target     │  • Policies   │  • Security │  • Processes │   │
│  │  • Gaps       │  • Training   │  • Privacy  │  • Evidence  │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                  │                                  │
│                                  ▼                                  │
│  [LAYER 5: VALIDATION]                                               │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    ANALYSIS VALIDATION                       │   │
│  │  □ Completeness  □ Currency    □ Jurisdiction Conflicts      │   │
│  │  □ Practicability□ Proportionality □ No Confirmation Bias    │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                  │                                  │
│                                  ▼                                  │
│  [LAYER 6: RECOMMENDATIONS]                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌────────────┐ │
│  │   Short     │  │   Medium    │  │    Long     │  │ Resources  │ │
│  │   Term      │  │    Term     │  │    Term     │  │   & Owners │ │
│  │  (0-3M)     │  │   (3-12M)   │  │   (12M+)    │  │            │ │
│  └─────────────┘  └─────────────┘  └─────────────┘  └────────────┘ │
│                                  │                                  │
│                                  ▼                                  │
│  [LAYER 7: REFLECTION]                                               │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌────────────┐ │
│  │Uncertainty  │  │   Change    │  │  Scenario   │  │ Continuous │ │
│  │  Mapping    │  │  Triggers   │  │  Planning   │  │ Monitoring │ │
│  └─────────────┘  └─────────────┘  └─────────────┘  └────────────┘ │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

## Anwendung mit komplexem Beispiel

### Szenario: Einführung einer KI-basierten Kreditscoring-Plattform

**Input:**
```
Vorhaben: KI-Plattform für automatisierte Kreditwürdigkeitsprüfung
Branche: Finanzdienstleistungen (Fintech)
Jurisdiktionen: Deutschland, Frankreich, Niederlande (EU-weit geplant)
Beteiligte: Fintech-Startup, Partnerbanken, Endkunden
Zeithorizont: 12 Monate bis Markteinführung
Budget: €500.000 für Compliance
```

**Erwartete CoT-Ausgabe:**

### Schritt 3: Tree-of-Thoughts Exploration

```
PFAD A: REGULATORISCHES RISIKO (Wahrscheinlichkeit: HOCH, Impact: KRITISCH)
┌─────────────────────────────────────────────────────────────┐
│ Trigger: EU AI Act tritt vollständig in Kraft (2026)        │
│                                                             │
│ Impact-Analyse:                                             │
│ • Kreditscoring = "High-Risk AI System" (Anhang III)        │
│ • Anforderungen:                                            │
│   - Conformity Assessment                                   │
│   - CE-Kennzeichnung                                        │
│   - Risk Management System                                  │
│   - Daten Governance                                        │
│   - Transparenzpflichten                                    │
│   - Menschliche Aufsicht                                    │
│                                                             │
│ Wahrscheinlichkeit: 95% (Gesetz bereits verabschiedet)      │
│ Impact: Ohne Compliance keine Markteinführung möglich       │
│                                                             │
│ Mitigation:                                                 │
│ • AI Act Compliance-Programm sofort starten                 │
│ • Notified Body frühzeitig identifizieren                   │
│ • Technical Documentation vorbereiten                       │
│ • Budget-Anpassung: +€200.000                               │
│                                                             │
│ Residualrisiko: Niedrig (bei rechtzeitiger Umsetzung)       │
└─────────────────────────────────────────────────────────────┘

PFAD B: HAFTUNGSRISIKO (Wahrscheinlichkeit: MITTEL, Impact: HOCH)
┌─────────────────────────────────────────────────────────────┐
│ Trigger: Fehlerhafte Kreditentscheidung führt zu            │
│          wirtschaftlichem Schaden                           │
│                                                             │
│ Szenarien:                                                  │
│ • Diskriminierung durch Algorithmic Bias                    │
│ • Falsch-negative (Kreditverweigerung an Kreditwürdigen)    │
│ • Falsch-positive (Kreditgewährung an Insolvenzgefährdete)  │
│                                                             │
│ Rechtliche Grundlagen:                                      │
│ • DSGVO Art. 22 (Automatisierte Entscheidungen)             │
│ • AGG (Allgemeines Gleichbehandlungsgesetz)                 │
│ • BGB (Vertragsschuldrecht)                                 │
│ • Produkthaftungsrecht                                      │
│                                                             │
│ Wahrscheinlichkeit: 40% (über 5 Jahre)                      │
│ Impact: €500K - €5M pro Fall + Reputation                   │
│                                                             │
│ Mitigation:                                                 │
│ • Algorithmic Fairness Testing (statistische Parität)       │
│ • Explainable AI (XAI) für Nachvollziehbarkeit              │
│ • Menschliche Überprüfung bei Grenzfällen                   │
│ • Haftpflichtversicherung (Tech E&O)                        │
│ • Klare AGB und Widerrufsbelehrung                          │
│                                                             │
│ Residualrisiko: Mittel                                      │
└─────────────────────────────────────────────────────────────┘

PFAD C: VERTRAGSRISIKO (Wahrscheinlichkeit: NIEDRIG-MITTEL, Impact: MITTEL)
┌─────────────────────────────────────────────────────────────┐
│ Trigger: Partnerbank beendet Kooperation oder verletzt      │
│          Exklusivitätsklausel                               │
│                                                             │
│ Szenarien:                                                  │
│ • Partnerbank entwickelt eigene Lösung                      │
│ • Regulatorische Probleme der Partnerbank                   │
│ • Streit über Revenue-Sharing                               │
│                                                             │
│ Wahrscheinlichkeit: 25% (über Vertragslaufzeit)             │
│ Impact: 30-50% Umsatzeinbruch, Kundenabwanderung            │
│                                                             │
│ Mitigation:                                                 │
│ • Multi-Partner-Strategie (nicht exklusiv)                  │
│ • Lange Kündigungsfristen (24 Monate)                       │
│ • Daten-Portabilität sicherstellen                          │
│ • Exit-Klauseln mit Übergangsfristen                        │
│                                                             │
│ Residualrisiko: Niedrig                                     │
└─────────────────────────────────────────────────────────────┘

EMPFIEHLUNG: Primärer Fokus auf PFAD A (AI Act Compliance),
sekundär PFAD B (Haftungsmanagement)
```

### Schritt 4: Gap-Analyse

```
AI ACT COMPLIANCE STATUS:
┌──────────────────────┬──────────┬──────────┬─────────────────────────────┐
│ Anforderung          │ Status   │ Priorität│ Maßnahme                    │
├──────────────────────┼──────────┼──────────┼─────────────────────────────┤
│ Risk Management      │ ❌ Fehlt │ P0       │ ISO 31000 + AI-spezifisch   │
│ System               │          │          │ implementieren              │
├──────────────────────┼──────────┼──────────┼─────────────────────────────┤
│ Data Governance      │ ⚠️ Teilw.│ P0       │ Trainingsdaten-Doku, Bias   │
│                      │          │          │ Testing, Datenqualität      │
├──────────────────────┼──────────┼──────────┼─────────────────────────────┤
│ Technical Doc.       │ ❌ Fehlt │ P0       │ Vollständige Doku erstellen │
├──────────────────────┼──────────┼──────────┼─────────────────────────────┤
│ Record-Keeping       │ ⚠️ Teilw.│ P1       │ Audit-Logs erweitern        │
├──────────────────────┼──────────┼──────────┼─────────────────────────────┤
│ Transparency         │ ❌ Fehlt │ P0       │ User-Information,           │
│                      │          │          │ Explainability-Features     │
├──────────────────────┼──────────┼──────────┼─────────────────────────────┤
│ Human Oversight      │ ⚠️ Teilw.│ P1       │ Override-Mechanismen,       │
│                      │          │          │ Schulung                    │
├──────────────────────┼──────────┼──────────┼─────────────────────────────┤
│ Accuracy/Robustness  │ ⚠️ Teilw.│ P1       │ Testing-Protokolle,         │
│                      │          │          │ Validation                  │
├──────────────────────┼──────────┼──────────┼─────────────────────────────┤
│ Cybersecurity        │ ✅ Vorh. │ P2       │ ISO 27001 bereits           │
│                      │          │          │ zertifiziert                │
└──────────────────────┴──────────┴──────────┴─────────────────────────────┘

DSGVO COMPLIANCE:
┌──────────────────────┬──────────┬──────────────────────────────────────┐
│ Anforderung          │ Status   │ Hinweis                              │
├──────────────────────┼──────────┼──────────────────────────────────────┤
│ Rechtsgrundlage      │ ⚠️ Prüfen│ Berechtigtes Interesse vs.           │
│ Art. 6               │          │ Einwilligung klären                  │
├──────────────────────┼──────────┼──────────────────────────────────────┤
│ Art. 22 (Autom.      │ ❌ Fehlt │ Widerspruchsrecht, menschliche       │
│ Entscheidungen)      │          │ Eingriffsmöglichkeit implementieren  │
├──────────────────────┼──────────┼──────────────────────────────────────┤
│ Art. 13/14 (Info-    │ ⚠️ Teilw.│ Spezifische Informationen für        │
│ pflichten)           │          │ Kreditscoring ergänzen               │
├──────────────────────┼──────────┼──────────────────────────────────────┤
│ Art. 35 (DPIA)       │ ❌ Fehlt │ Pflichtige DPIA durchführen          │
└──────────────────────┴──────────┴──────────────────────────────────────┘
```

### Schritt 5: Self-Consistency Check

```
VALIDIERUNG:

Vollständigkeit: ✓ PASS
• Alle relevanten EU-Verordnungen (AI Act, DSGVO, DORA) berücksichtigt
• Nationale Umsetzungen (BDSG) eingeschlossen
• Branchenspezifisch (MaRisk, BAIT) geprüft

Aktualität: ✓ PASS
• AI Act Stand: Verabschiedet, Phasenweise Inkrafttreten
• DORA: Ab Januar 2025 anwendbar
• Neueste BGH-Rechtsprechung zu Kreditvergabe berücksichtigt

Jurisdiktion: ⚠️ ATTENTION
• Frankreich: Zusätzliche CNIL-Vorgaben zu beachten
• Niederlande: AP-Richtlinien für Algorithmen
→ Empfehlung: Jurisdiction-spezifische Analysen durch lokale Counsel

Praktikabilität: ✓ PASS
• Empfohlene Maßnahmen sind mit Budget umsetzbar
• Timeline von 12 Monaten ist realistisch für P0/P1

Proportionalität: ✓ PASS
• Compliance-Aufwand (~€700K) steht im Verhältnis zum 
  Geschäftswert und Risiko

Cognitive Bias-Check:
✓ Keine Confirmation Bias: Gegenteilige Rechtsauffassungen 
  (z.B. hinsichtlich Art. 22 DSGVO) berücksichtigt
✓ Kein Overconfidence: Risiken konservativ eingeschätzt
✓ Kein Recency Bias: Historische Präzedenzfälle (Schufa-Urteile) 
  einbezogen
```

## Variationen für verschiedene Komplexitätsstufen

### Level 1: Foundation (Quick Check)
```
Bewerte die rechtlichen Risiken von [VORHABEN] in [JURISDIKTION].

1. Hauptanwendbare Gesetze identifizieren
2. Kritische Compliance-Anforderungen
3. Top 3 Risiken mit Mitigation

Ausgabe: 2-seitige Risiko-Übersicht
```

### Level 2: Professional (Standard)
```
[Standard-Prompt wie oben]

Zusätzlich:
- Detaillierte Pflichten-Matrix
- Gap-Analyse
- Implementierungs-Roadmap
```

### Level 3: Elite (Full Prompt)
```
[Vollständiger Prompt mit allen 7 Schritten]

Zusätzliche Anforderungen:
- Multi-Jurisdiktions-Analyse
- Detaillierte Vertragsgestaltung
- Regulatorisches Engagement-Plan
- DPIA/PIA (Data Protection Impact Assessment)
- Whistleblowing-System-Bewertung
```

### Level 4: Masterclass (Global Enterprise)
```
[Elite-Level] +

Erweiterungen:
- Global Privacy Framework (GDPR, CCPA, LGPD, PIPL, etc.)
- International Data Transfers (SCCs, adequacy decisions)
- Antitrust/Competition Law Analyse
- M&A-Readiness (Due Diligence Vorbereitung)
- Regulatory Engagement Strategy (Lobbying, Public Affairs)
- Cross-Border Investigation Response
- International Arbitration Klauseln
```

## Prompt-Metadaten

| Attribut | Wert |
|----------|------|
| Komplexität | ★★★★★ |
| Token-Schätzung | 4.000-9.000 |
| Ausführungszeit | 20-50 Minuten |
| Domäne | Recht / Compliance / Regulatorik |
| Beste Modelle | Claude 3.5 Sonnet, GPT-4, Kimi K2.5 |

## Erfolgskriterien

- [ ] Alle 7 Denkschritte explizit durchlaufen
- [ ] Mindestens 3 Risiko-Szenarien exploriert
- [ ] Quantifizierte Risiko-Bewertung (Wahrscheinlichkeit × Impact)
- [ ] Gap-Analyse mit Priorisierung
- [ ] Self-Consistency Check gegen Cognitive Biases
- [ ] Konkrete, umsetzbare Handlungsempfehlungen
- [ ] Continuous Monitoring Konzept
- [ ] Disclaimer: Keine Rechtsberatung

## Wichtiger Hinweis

> **Disclaimer:** Dieser Prompt dient der strukturierten Analyse 
> rechtlicher und compliance-relevanter Fragestellungen. Die 
> Ausgabe eines KI-Systems stellt keine Rechtsberatung dar. 
> Für verbindliche Rechtsauskünfte ist stets ein qualifizierter 
> Rechtsanwalt zu konsultieren.
