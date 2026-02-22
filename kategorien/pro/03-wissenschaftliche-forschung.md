---
id: "#082"
titel: "Wissenschaftliche Forschungsplanung & Experimentdesign"
kategorie: "Pro"
unterkategorie: "Forschungsmethodik & Wissenschaft"
tags: ["Forschung", "Experimentdesign", "Hypothesentest", "Statistik", "CoT", "ToT", "Reflection"]
erstellt: "2026-02-21"
plattformen: ["Claude", "GPT-4", "Kimi", "Gemini"]
autor: "LYRA Prompt Engineering"
version: "1.0.0"
---

# Wissenschaftliche Forschungsplanung & Experimentdesign

## Prompt

```
Du bist ein erfahrener Principal Investigator mit 20+ Jahren Erfahrung in 
interdisziplinärer Forschung. Entwickle einen vollständigen Forschungsplan 
für folgendes Vorhaben:

**FORSCHUNGSKONTEXT:**
Disziplin: [HAUPTDISZIPLIN]
Subdisziplin: [SPEZIALGEBIET]
Forschungsfrage: [KERNFORSCHUNGSFRAGE]
Hypothese: [HAUPTHYPOTHESE]
Zeitrahmen: [MONATE/JAHRE]
Budget: [FÖRDERBETRAG]
Team-Größe: [ANZAHL FORSCHER]

**DEINE AUFGABE:**
Entwickle einen publikationsreifen Forschungsplan durch systematisches 
Multi-Layer-Reasoning.

**CHAIN-OF-THOUGHT ANWEISUNG:**

[SCHRITT 1: FORSCHUNGSLÜCKEN-ANALYSE]
Explizite Analyse des aktuellen Standes:
- Systematische Literaturrecherche-Strategie
- Identifikation von 3-5 relevanten Forschungsströmungen
- Mapping der theoretischen Grundlagen
- Identifikation der spezifischen Forschungslücke
- Begründung der Relevanz (theoretisch + praktisch)

[SCHRITT 2: THEORIE-ENTWICKLUNG]
Entwickle das theoretische Gerüst:
- Haupttheorie(n) und deren Anwendung
- Konzeptuelle Modellierung
- Definition aller Konstrukte
- Operationalisierungsstrategie
- Theoretische Propositionen ableiten

[SCHRITT 3: TREE-OF-THOUGHTS: METHODISCHE PFADE]
Exploriere 3 alternative methodologische Ansätze:

PFAD A: Quantitatives Design (Experimentell/Quasi-Experimentell)
- Randomisierte Kontrollgruppen-Studie
- Große Stichprobe (n > 500)
- Strukturgleichungsmodellierung
→ Stärken: Kausalität, Generalisierbarkeit
→ Schwächen: External Validity, Kontext-Verlust

PFAD B: Qualitatives Design (Ethnographisch/Fallstudien)
- Tiefgehende Einzelfall- oder Mehrfachfallanalyse
- Theoretisches Sampling
- Grounded Theory-Ansatz
→ Stärken: Kontext-Tiefe, emergente Muster
→ Schwächen: Generalisierbarkeit, Forscher-Bias

PFAD C: Mixed-Methods Design (Konvergent/Explorativ/Explanativ)
- Parallele oder sequentielle Quant+Qual Integration
- Methodologische Triangulation
- Embedded Design
→ Stärken: Komplementarität, vollständigeres Bild
→ Schwächen: Komplexität, Ressourcen-Intensität

Für jeden Pfad detailliere:
- Exakte Methodologie und Design-Typ
- Stichproben-Strategie und Größenberechnung
- Datenerhebungsinstrumente
- Analyse-Verfahren
- Validitäts- und Reliabilitäts-Strategien
- Zeitplan und Meilensteine

[SCHRITT 4: EXPERIMENTDESIGN-DETAILLIERUNG]
Für den empfohlenen Pfad, spezifiziere:

a) Studiendesign:
   - Design-Typ (Between-Subject/Within-Subject/Mixed)
   - Faktoren und Stufen
   - Experimental-Manipulationen
   - Kontrollvariablen
   - Randomisierungsstrategie

b) Stichprobe:
   - Zielpopulation und Zugang
   - Inklusions-/Exklusionskriterien
   - Stichprobengröße (Power-Analyse)
   - Rekrutierungsstrategie
   - Vergütung/Ethik

c) Variablen:
   - Unabhängige Variable(n): Definition, Manipulation, Checks
   - Abhängige Variable(n): Messung, Skalierung, Validierung
   - Moderator-Variablen: Hypothesen und Messung
   - Mediator-Variablen: Kausale Mechanismen
   - Kontrollvariablen: Confounds und Handling

d) Prozedur:
   - Session-Ablauf (Timeline)
   - Instruktionen und Framing
   - Debriefing-Protokoll
   - Qualitätskontrollen (Attention Checks, Manipulation Checks)

[SCHRITT 5: SELF-CONSISTENCY CHECK]
Validiere das Design gegen wissenschaftliche Standards:

□ Interne Validität: Sind Confounds kontrolliert?
□ Externe Validität: Ist Generalisierbarkeit gegeben?
□ Konstruktvalidität: Messen wir was wir messen wollen?
□ Statistische Validität: Ist die Power ausreichend?
□ Ökologische Validität: Ist das Setting realistisch?

Prüfe auf methodische Fehler:
□ Keine HARKing (Hypothesizing After Results are Known)
□ Keine p-Hacking
□ Keine Optional Stopping
□ Transparente Daten-Exklusionskriterien
□ Pre-Registration Plan

[SCHRITT 6: ANALYSE-PLAN]
Detaillierter Analyse-Workflow:

- Datenaufbereitung: Cleaning, Transformation, Missing Data
- Deskriptive Statistik: Mittelwerte, SD, Verteilungen
- Inferenzstatistik: Hauptanalysen, Post-hoc Tests
- Sensitivitätsanalysen: Robustheit der Ergebnisse
- Exploratorische Analysen: Explizit als solche gekennzeichnet
- Visualisierungen: Abbildungsplan
- Software: R/Python/SPSS mit Packages

[SCHRITT 7: REFLECTION & ITERATION]
Selbstkritische Analyse:

- Was ist die größte methodische Schwäche des Designs?
- Welche alternativen Erklärungen für erwartete Effekte gibt es?
- Wie würde sich das Design ändern bei:
  * Nicht-signifikanten Ergebnissen?
  * Überraschenden Befunden?
  * Problemen bei der Rekrutierung?
  * Budget-Kürzungen um 30%?

- Welche Pilot-Studien sind vor dem Hauptexperiment nötig?
- Was sind die größten ethischen Bedenken?
- Wie könnten die Ergebnisse falsch interpretiert werden?

**AUSGABEFORMAT:**

## Executive Summary
[1-seitige Zusammenfassung: Kernfrage, Methode, erwarteter Beitrag]

## Theoretischer Rahmen
[Konzeptuelles Modell, Hypothesen, Propositionen]

## Methodologie
[Detaillierte Beschreibung des gewählten Designs]

## Experimentdesign
[Alle Spezifikationen aus Schritt 4]

## Analyse-Plan
[Statistische Verfahren und Workflow]

## Zeitplan & Meilensteine
[Gantt-Chart oder Tabellarisch]

## Risiko-Management
[Mögliche Probleme und Contingency-Pläne]

## Publikations-Strategie
[Zieljournale, Konferenzen, Open Science Plan]
```

## Chain-of-Thought Struktur

```
┌─────────────────────────────────────────────────────────────────────┐
│           SCIENTIFIC RESEARCH PLANNING REASONING                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  [LAYER 1: LITERATURE & GAP ANALYSIS]                                │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │  Systematic │  │  Research   │  │ Theoretical │  │  Relevance  │ │
│  │   Review    │  │  Streams    │  │  Mapping    │  │  Justify    │ │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘ │
│         └─────────────────┴─────────────────┴─────────────────┘      │
│                              │                                       │
│                              ▼                                       │
│  [LAYER 2: THEORY DEVELOPMENT]                                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │   Theory    │  │ Conceptual  │  │ Construct   │  │ Theoretical │ │
│  │ Selection   │  │   Model     │  │ Definitions │  │Propositions │ │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘ │
│         └─────────────────┴─────────────────┴─────────────────┘      │
│                              │                                       │
│                              ▼                                       │
│  [LAYER 3: TREE-OF-THOUGHTS]                                         │
│              ┌───────────────────────────────────────┐              │
│              │      METHODOLOGICAL DECISION TREE      │              │
│              │                   │                    │              │
│         ┌────┴────┐         ┌────┴────┐         ┌────┴────┐        │
│         │  PFAD A │         │  PFAD B │         │  PFAD C │        │
│         │Quantitat│         │Qualitativ│         │Mixed-   │        │
│         │  (n>500)│         │(Deep Dive)│        │Methods  │        │
│         │         │         │         │         │         │        │
│         │✓ Causal │         │✓ Context│         │✓ Complete│        │
│         │✗ Context│         │✗ General│         │✗ Complex │        │
│         └────┬────┘         └────┬────┘         └────┬────┘        │
│              └───────────────────┼───────────────────┘              │
│                                  │                                  │
│                    ┌─────────────┴─────────────┐                   │
│                    │   MULTI-CRITERIA SCORING   │                   │
│                    │  Validity × Feasibility    │                   │
│                    └─────────────┬─────────────┘                   │
│                                  │                                  │
│                                  ▼                                  │
│  [LAYER 4: EXPERIMENTAL DESIGN]                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Study Design  │   Sample     │  Variables  │  Procedure   │   │
│  │  • Between/Within│  • Power    │  • IV/DV    │  • Timeline  │   │
│  │  • Factors      │    Analysis │  • Moderator│  • Debrief   │   │
│  │  • Controls     │  • Recruit. │  • Mediator │  • Quality   │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                  │                                  │
│                                  ▼                                  │
│  [LAYER 5: VALIDATION]                                              │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    VALIDITY CHECKLIST                        │   │
│  │  □ Internal   □ External   □ Construct   □ Statistical      │   │
│  │  □ No HARKing □ No p-hack  □ Pre-reg.    □ Transparent      │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                  │                                  │
│                                  ▼                                  │
│  [LAYER 6: ANALYSIS PLAN]                                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌────────────┐ │
│  │   Data      │  │ Descriptive │  │ Inferential │  │Sensitivity │ │
│  │  Cleaning   │  │  Statistics │  │  Statistics │  │  Analysis  │ │
│  └─────────────┘  └─────────────┘  └─────────────┘  └────────────┘ │
│                                  │                                  │
│                                  ▼                                  │
│  [LAYER 7: REFLECTION]                                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌────────────┐ │
│  │  Method.    │  │ Alternative │  │  Scenario   │  │  Pilot     │ │
│  │  Weakness   │  │Explanations │  │  Planning   │  │  Needs     │ │
│  └─────────────┘  └─────────────┘  └─────────────┘  └────────────┘ │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

## Anwendung mit komplexem Beispiel

### Szenario: KI-gestützte kreative Problemlösung in Teams

**Input:**
```
Disziplin: Arbeits- und Organisationspsychologie
Subdisziplin: Kreativitätsforschung / Human-AI Interaction
Forschungsfrage: Wie beeinflusst die Integration von KI-Tools 
                die kreative Leistung und Teamdynamik in 
                interdisziplinären Innovationsprozessen?
Hypothese: Teams mit KI-Unterstützung zeigen höhere kreative 
           Leistung, aber geringere Team-Kohäsion
Zeitrahmen: 24 Monate
Budget: €450.000
Team-Größe: 1 PI, 2 Doktoranden, 1 PostDoc
```

**Erwartete CoT-Ausgabe:**

### Schritt 3: Tree-of-Thoughts Exploration

```
PFAD A: Quantitatives Laborexperiment
┌─────────────────────────────────────────────────────────────┐
│ Design: 2×2 Between-Subjects Design                          │
│   • Faktor 1: KI-Unterstützung (Ja/Nein)                     │
│   • Faktor 2: Team-Diversität (Hoch/Niedrig)                 │
│   • n = 320 Teilnehmer (80 Teams à 4 Personen)               │
│                                                              │
│ Messung:                                                     │
│   • Kreativität: TTCT, konsensuale Bewertung                 │
│   • Team-Kohäsion: Group Environment Questionnaire           │
│   • Prozess: Videocodierung, Log-Daten                       │
│                                                              │
│ Analyse: MANOVA, Mediationsanalyse (PROCESS)                 │
│                                                              │
│ Scoring:                                                     │
│   • Interne Validität: 9/10                                  │
│   • Externe Validität: 5/10 (Artifizielles Setting)          │
│   • Machbarkeit: 7/10 (Aufwändige Rekrutierung)              │
└─────────────────────────────────────────────────────────────┘

PFAD B: Qualitative Feldstudie
┌─────────────────────────────────────────────────────────────┐
│ Design: Multiple Embedded Case Studies                       │
│   • 6 Unternehmen, jeweils 2-3 Teams                         │
│   • 6 Monate Beobachtungszeitraum pro Team                   │
│                                                              │
│ Datenerhebung:                                               │
│   • Teilnehmende Beobachtung (Workshops, Meetings)           │
│   • Tiefeninterviews (n = 30-40)                             │
│   • Dokumentenanalyse (Konzepte, Kommunikation)              │
│                                                              │
│ Analyse: Thematische Analyse (Braun & Clarke)                │
│                                                              │
│ Scoring:                                                     │
│   • Interne Validität: 6/10 (Keine Kausalität)               │
│   • Externe Validität: 9/10 (Real-world Setting)             │
│   • Machbarkeit: 6/10 (Zeitintensiv, Zugang schwierig)       │
└─────────────────────────────────────────────────────────────┘

PFAD C: Mixed-Methods (Explanatory Sequential)
┌─────────────────────────────────────────────────────────────┐
│ Design: QUAN → qual                                          │
│   • Phase 1: Quasi-Experiment (n = 200 in 50 Teams)          │
│   • Phase 2: Fallstudien zur Erklärung (n = 4 Teams)         │
│                                                              │
│ Integration:                                                 │
│   • Joint Display: Quantitative Befunde + qualitative        │
│     Erklärungen nebeneinander                                │
│   • Follow-up: Qualitative Interviews zu überraschenden      │
│     quantitativen Ergebnissen                                │
│                                                              │
│ Scoring:                                                     │
│   • Interne Validität: 7/10                                  │
│   • Externe Validität: 8/10                                  │
│   • Machbarkeit: 6/10 (Ressourcen-intensiv)                  │
│   • Innovationsgrad: 9/10 (Neue Methodik für Feld)           │
└─────────────────────────────────────────────────────────────┘

EMPFIEHLUNG: PFAD C (Mixed-Methods)
Begründung: Beste Balance aus rigoroser Kausalanalyse und 
realistischer Kontextualisierung für ein emergentes Forschungsfeld
```

### Schritt 4: Experimentdesign-Detail

```
STUDIENDESIGN:
┌────────────────────────────────────────────────────────────┐
│ Type: Quasi-experimentell (Keine Randomisierung möglich)   │
│                                                            │
│ Faktoren:                                                  │
│   • KI-Unterstützung (Treatment: KI-Tool vs. Control:      │
│     traditionelle Methoden)                                │
│   • Aufgabenkomplexität (Hoch vs. Niedrig) - within        │
│                                                            │
│ Design: Mixed 2 × 2 × 2                                    │
│   • Between: KI vs. Control                                │
│   • Within: Komplexität (counterbalanced)                  │
│   • Between: Team-Zusammensetzung                          │
│                                                            │
│ Randomisierung:                                            │
│   • Teams werden basierend auf Matching-Variablen          │
│     (Teamgröße, Branche, Erfahrung) Treatment/Control      │
│     zugeordnet                                             │
│   • Aufgaben-Reihenfolge innerhalb Teams randomisiert      │
└────────────────────────────────────────────────────────────┘

STICHPROBE:
┌────────────────────────────────────────────────────────────┐
│ Power-Analyse (G*Power):                                   │
│   • Effektstärke: f = 0.25 (medium)                        │
│   • α = 0.05, Power = 0.80                                 │
│   • Gruppen: 4 (2 × 2)                                     │
│   → Benötigt: n = 200 (50 Teams à 4 Personen)              │
│   → Geplant: n = 240 (60 Teams) für Dropout                │
│                                                            │
│ Rekrutierung:                                              │
│   • Partner: 3 Innovations-Agenturen, 2 Unternehmen        │
│   • Incentives: €150 pro Person, Team-Ergebnis-Prämie      │
│   • Kanäle: LinkedIn, Fachverbände, Unternehmensnetzwerke  │
│                                                            │
│ Inklusionskriterien:                                       │
│   • Mindestens 2 Jahre Berufserfahrung                     │
│   • Regelmäßige Teamarbeit (>50% Arbeitszeit)              │
│   • Keine vorherige Nutzung des spezifischen KI-Tools      │
└────────────────────────────────────────────────────────────┘

VARIABLEN:
┌────────────────────────────────────────────────────────────┐
│ Unabhängige Variable (Treatment):                          │
│   • KI-Unterstützung: Zugang zu GPT-4-basiertem            │
│     Brainstorming-Tool vs. traditionelle Whiteboard-       │
│     Methode                                                │
│   • Manipulation Check: Nutzungsdaten, Exit-Interview      │
│                                                            │
│ Abhängige Variablen:                                       │
│   • Kreative Leistung:                                     │
│     - Fluency (Anzahl Ideen)                               │
│     - Flexibility (Kategorienbreite)                       │
│     - Originality (Seltenheit × Neuheit)                   │
│     - Nutzen (Expert-Ratings)                              │
│   • Team-Kohäsion: GEQ-Skala (Carless & De Paola)          │
│   • Prozess-Qualität: Kommunikationsanalyse (LINCS)        │
│                                                            │
│ Moderator:                                                 │
│   • KI-Bereitschaft: Pre-Survey (5 Items, 7-Punkt)         │
│                                                            │
│ Mediator:                                                  │
│   • Kognitive Last: NASA-TLX                               │
│   • Transaktives Gedächtnis: Knowledge-Maps                │
│                                                            │
│ Kontrollvariablen:                                         │
│   • Team-Tenure, Branche, Aufgabenvertrautheit             │
│   • Zeitdruck, Raum, Tageszeit                             │
└────────────────────────────────────────────────────────────┘
```

### Schritt 5: Self-Consistency Check

```
VALIDITÄTS-PRÜFUNG:

Interne Validität:
┌────────────────────────────────────────────────────────────┐
│ Bedrohungen und Kontrollen:                                │
│ ✓ Selection Bias: Matching auf Team-Eigenschaften          │
│ ✓ History: Kurze Sessions (2h), gleicher Zeitraum          │
│ ✓ Maturation: Keine langen Zeiträume                       │
│ ✓ Testing: Keine Pre-Tests für Kreativitätsaufgaben        │
│ ✓ Instrumentation: Standardisierte Tools                   │
│ ✓ Attrition: Dropout-Ersatz geplant                        │
│ ⚠ Regression: Kontrolle durch Baseline-Messung             │
└────────────────────────────────────────────────────────────┘

Anti-Pattern-Check:
✓ Hypothesen vor Datenerhebung formuliert
✓ Stichprobengröße vor Analyse festgelegt
✓ Exklusionskriterien dokumentiert (keine HARKing)
✓ Pre-Registration geplant (OSF)
✓ Alle Variablen in Analyseplan aufgeführt
✓ Exploratorische Analysen separat gekennzeichnet
```

## Variationen für verschiedene Komplexitätsstufen

### Level 1: Foundation (Kurzfristiges Projekt)
```
Entwickle einen Forschungsplan für [FORSCHUNGSFRAGE].

Berücksichtige:
1. Kernhypothese und theoretische Basis
2. Methodische Wahl (quantitativ/qualitativ/mixed)
3. Stichprobengröße und Rekrutierung
4. Hauptanalyse-Verfahren

Ausgabe: 2-seitiger Forschungsüberblick
```

### Level 2: Professional (Standard)
```
[Standard-Prompt wie oben]

Zusätzlich:
- Detailliertes Experimentdesign
- Vollständiger Analyse-Plan
- Zeitplan mit Meilensteinen
```

### Level 3: Elite (Full Prompt)
```
[Vollständiger Prompt mit allen 7 Schritten]

Zusätzliche Anforderungen:
- Open Science Plan (Daten, Code, Materialien)
- Publikations-Strategie mit Zieljournals
- Ethik-Antrag-Vorlage
- Budget-Detailplanung
- Risiko-Management mit Contingencies
```

### Level 4: Masterclass (Large-Scale Research)
```
[Elite-Level] +

Erweiterungen:
- Multi-Site Koordination (verschiedene Länder/Institutionen)
- Longitudinales Design mit Retention-Strategie
- Komplexe Interventionsstudie (RCT)
- Bayesianische Analyse-Planung
- Machine Learning für Pattern Detection
- Stakeholder-Engagement-Strategie
- Impact- und Transfer-Planung
```

## Prompt-Metadaten

| Attribut | Wert |
|----------|------|
| Komplexität | ★★★★★ |
| Token-Schätzung | 4.000-9.000 |
| Ausführungszeit | 20-50 Minuten |
| Domäne | Wissenschaftliche Forschung |
| Beste Modelle | Claude 3.5 Sonnet, GPT-4, Kimi K2.5 |

## Erfolgskriterien

- [ ] Alle 7 Denkschritte explizit durchlaufen
- [ ] Mindestens 3 methodische Pfade verglichen
- [ ] Power-Analyse für Stichprobengröße
- [ ] Validitäts-Check gegen wissenschaftliche Standards
- [ ] Anti-Patterns explizit vermieden
- [ ] Reflexion über methodische Schwächen
- [ ] Pre-Registration Plan berücksichtigt
