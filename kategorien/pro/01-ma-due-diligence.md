---
titel: "M&A Due Diligence & Valuation Strategie"
kategorie: "Pro"
unterkategorie: "Finanzanalyse & Unternehmensbewertung"
tags: ["M&A", "Due-Diligence", "Valuation", "DCF", "LBO", "Strategie", "CoT", "ToT"]
erstellt: "2026-02-21"
plattformen: ["Claude", "GPT-4", "Kimi", "Gemini"]
autor: "LYRA Prompt Engineering"
version: "1.0.0"
---

# M&A Due Diligence & Valuation Strategie

## Prompt

```
Du bist ein Senior M&A-Berater mit 20+ Jahren Erfahrung in Transaktionen >$500M. 
Führe eine vollständige Due-Diligence und Bewertung durch.

**KONTEXT:**
Zielunternehmen: [UNTERNEHMEN BESCHREIBEN]
Branche: [BRANCHE]
Transaktionstyp: [AKQUISITION/FUSION/MBO]
Strategische Motivation: [SYNERGIEN/MARKTZUGANG/TECHNOLOGIE]

**DEINE AUFGABE:**
Analysiere diese M&A-Opportunity durch systematische Multi-Layer-Reasoning.

**CHAIN-OF-THOUGHT ANWEISUNG:**
Arbeite EXPLIZIT in folgenden Denkschritten:

[SCHRITT 1: STRATEGISCHE ALIGNMENT-ANALYSE]
- Bewerte strategische Fit-Matrix (1-10 Skala)
- Identifiziere 3 Kernsynergien mit Quantifizierung
- Analysiere kulturelle Kompatibilität

[SCHRITT 2: FINANZIELLE DUE-DILIGENCE]
- Historische Performance (3-5 Jahre)
- Qualität der Einnahmen (Recurring vs. One-time)
- Working Capital Analyse
- Capex-Anforderungen

[SCHRITT 3: BEWERTUNGSMODELLIERUNG]
→ DCF-Analyse mit 3 Szenarien (Base/Bull/Bear)
→ Comparable Company Analysis
→ Precedent Transaction Analysis
→ LBO-Fähigkeit (falls relevant)

[SCHRITT 4: RISIKO-ASSESSMENT]
- Identifiziere Top 5 Deal-Breaker-Risiken
- Bewerte Eintrittswahrscheinlichkeit & Impact
- Entwickle Mitigationsstrategien

[SCHRITT 5: TREE-OF-THOUGHTS EXPLORATION]
Exploriere 3 alternative Strategiepfade:
→ PFAD A: Vollständige Akquisition
→ PFAD B: Minority Investment + Option
→ PFAD C: Strategische Partnerschaft statt Akquisition

Vergleiche jeden Pfad nach:
- Risiko-Adjustierter Rendite
- Strategischer Kontrolle
- Implementierungskomplexität
- Exit-Optionen

[SCHRITT 6: SELF-CONSISTENCY CHECK]
Validiere deine Analyse:
□ Sind Annahmen konsistent über alle Modelle?
□ Stimmen Synergien mit historischen Vergleichstransaktionen überein?
□ Sind Risiken vollständig und nicht doppelt gezählt?
□ Ist die Bewertungsspanne angemessen breit?

[SCHRITT 7: REFLECTION & ITERATION]
- Was sind die größten Unsicherheiten in deiner Analyse?
- Welche zusätzlichen Informationen wären kritisch?
- Wie würde sich deine Empfehlung ändern bei:
  * 20% niedrigerem EBITDA?
  * Verzögerung der Integration um 12 Monate?
  * Verlust eines Key-Kunden (>10% Umsatz)?

**AUSGABEFORMAT:**

## Executive Summary
[1-Seitige Zusammenfassung mit klarem GO/NO-GO Empfehlung]

## Detaillierte Analyse
[Strukturiert nach den 7 Schritten oben]

## Bewertungsmatrix
| Methode | Low | Base | High | Gewichtung |
|---------|-----|------|------|------------|
| DCF | | | | 40% |
| Comps | | | | 30% |
| Precedents | | | | 20% |
| LBO | | | | 10% |
| **Blended** | | | | 100% |

## Risiko-Heatmap
[Visualisierung: Eintrittswahrscheinlichkeit vs. Impact]

## Handlungsempfehlung
[Konkrete nächste Schritte mit Timeline und Verantwortlichen]

## Alternative Szenarien
[Wie verändert sich die Empfehlung bei veränderten Rahmenbedingungen?]
```

## Chain-of-Thought Struktur

```
┌─────────────────────────────────────────────────────────────────┐
│                    COHERENT REASONING FLOW                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [LAYER 1: STRATEGISCH]                                          │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐          │
│  │   Fit-Matrix │───→│  Synergien  │───→│ Kultur-Check │          │
│  └─────────────┘    └─────────────┘    └─────────────┘          │
│         │                  │                  │                  │
│         └──────────────────┼──────────────────┘                  │
│                            ▼                                     │
│  [LAYER 2: FINANZIELL]                                           │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐          │
│  │  Historical │───→│   Revenue   │───→│    WC &     │          │
│  │ Performance │    │   Quality   │    │    Capex    │          │
│  └─────────────┘    └─────────────┘    └─────────────┘          │
│                            │                                     │
│                            ▼                                     │
│  [LAYER 3: BEWERTUNG]         ┌─────────────────────┐           │
│  ┌─────────┐ ┌─────────┐     │   TRIANGULATION     │           │
│  │   DCF   │ │  Comps  │────→│      MATRIX         │           │
│  │ 3-Szen. │ │         │     │  (Convergence Test) │           │
│  └─────────┘ └─────────┘     └─────────────────────┘           │
│  ┌─────────┐ ┌─────────┐              │                         │
│  │Precedent│ │   LBO   │──────────────┘                         │
│  │ Trans.  │ │         │                                        │
│  └─────────┘ └─────────┘                                        │
│                            │                                     │
│                            ▼                                     │
│  [LAYER 4: RISIKO]                                               │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐          │
│  │   Risiko-   │───→│  Impact     │───→│ Mitigation  │          │
│  │ Identifik.  │    │  Bewertung  │    │ Strategien  │          │
│  └─────────────┘    └─────────────┘    └─────────────┘          │
│                            │                                     │
│                            ▼                                     │
│  [LAYER 5: TREE-OF-THOUGHTS]                                     │
│           ┌─────────────────────────────────┐                   │
│           │         STRATEGIE-BAUM          │                   │
│           │              │                  │                   │
│      ┌────┴────┐    ┌────┴────┐    ┌────┴────┐                │
│      │  PFAD A │    │  PFAD B │    │  PFAD C │                │
│      │Full Acq.│    │Minority │    │Partner- │                │
│      │         │    │+ Option │    │  schaft │                │
│      └────┬────┘    └────┬────┘    └────┬────┘                │
│           └─────────────────────────────────┘                   │
│                            │                                     │
│                            ▼                                     │
│  [LAYER 6: VALIDATION]    ┌─────────────────┐                   │
│                           │ CONSISTENCY-CHECK │                  │
│                           │  □ Annahmen       │                  │
│                           │  □ Synergien      │                  │
│                           │  □ Risiken        │                  │
│                           │  □ Spanne         │                  │
│                           └─────────────────┘                   │
│                            │                                     │
│                            ▼                                     │
│  [LAYER 7: REFLECTION]                                           │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐          │
│  │Unsicherheiten│───→│ Info-Gaps   │───→│ Sensitivität │          │
│  │  Identifik.  │    │   Mapping   │    │   Analyse    │          │
│  └─────────────┘    └─────────────┘    └─────────────┘          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Anwendung mit komplexem Beispiel

### Szenario: Tech-Unternehmen erwägt Akquisition eines SaaS-Startups

**Input:**
```
Zielunternehmen: CloudSync AI - B2B SaaS für Datenintegration
Branche: Enterprise Software / Data Integration
Transaktionstyp: Strategische Akquisition
Strategische Motivation: Technologie-Stack erweitern + Kundenbasis
Jährlicher Umsatz: $45M (YoY Growth: 85%)
EBITDA: $8M (18% Margin)
Kunden: 350 Enterprise-Kunden
```

**Erwartete CoT-Ausgabe:**

### Schritt 1: Strategische Alignment-Analyse
```
Fit-Matrix-Bewertung:
┌─────────────────────┬─────────┬─────────────────────────────┐
│ Dimension           │ Score   │ Begründung                  │
├─────────────────────┼─────────┼─────────────────────────────┤
│ Technologische Fit  │ 9/10    │ API-First passt zu unserer  │
│                     │         │ Microservices-Architektur   │
├─────────────────────┼─────────┼─────────────────────────────┤
│ Markt-Position      │ 8/10    │ Komplementärer Kundenstamm  │
├─────────────────────┼─────────┼─────────────────────────────┤
│ Kultureller Fit     │ 7/10    │ Agile Kultur, aber andere   │
│                     │         │ Entscheidungsgeschwindigkeit│
├─────────────────────┼─────────┼─────────────────────────────┤
│ Geografische Präsenz│ 6/10    │ 60% Overlap in EMEA         │
└─────────────────────┴─────────┴─────────────────────────────┘

Kernsynergien (quantifiziert):
1. Cross-Selling: $12M jährlich ab Jahr 3 (30% der Zielkunden)
2. Tech-Integration: $3M Einsparungen bei Lizenzkosten
3. Skaleneffekte: $2M Reduktion Cloud-Infrastruktur
```

### Schritt 5: Tree-of-Thoughts Exploration
```
PFAD A: Vollständige Akquisition ($180-220M)
   ✓ Vollständige Kontrolle über Technologie
   ✓ Schnellste Integration möglich
   ✗ Hohes Kapitalbindung
   ✗ Integrationsrisiko
   → Risiko-adjustierte IRR: 22%

PFAD B: 40% Minority + Call Option ($80M + $120M)
   ✓ Risikostreuung
   ✓ Alignment durch gemeinsame Ziele
   ✗ Komplexe Governance
   ✗ Begrenzte Synergien in Phase 1
   → Risiko-adjustierte IRR: 19%

PFAD C: Strategische Partnerschaft
   ✓ Kein Kapitalbindung
   ✓ Flexibilität
   ✗ Keine exklusive Technologie
   ✗ Wettbewerber könnten gleichen Zugang erhalten
   → Strategischer Wert: Mittel

EMPFIEHLUNG: PFAD A mit strukturiertem Earn-out (30% des Kaufpreises)
```

### Schritt 6: Self-Consistency Check
```
VALIDIERUNG:
□ Annahmen: Wachstumsraten (85% → 35% über 5 Jahre) konsistent 
  mit Marktdaten (Snowflake, Fivetran Vergleiche)
□ Synergien: $17M Gesamtsynergien = 38% des Umsatzes, im Range
  historischer SaaS-Akquisitionen (30-50%)
□ Risiken: Keine Doppelzählung, alle material (>5% Impact)
□ Bewertungsspanne: 4.0x-4.9x Revenue = angemessen für 
  Wachstumsstufe und Profitabilität
```

## Variationen für verschiedene Komplexitätsstufen

### Level 1: Foundation (30 Minuten)
```
Führe eine Due-Diligence durch für [UNTERNEHMEN].

Konzentriere dich auf:
1. Strategischen Fit (Score 1-10)
2. Schnelle Bewertung (Comps-Methode)
3. Top 3 Risiken

Ausgabe: 1-seitige Zusammenfassung mit GO/NO-GO
```

### Level 2: Professional (2 Stunden)
```
[Standard-Prompt wie oben]

Zusätzlich:
- DCF mit 2 Szenarien
- Einfache Risiko-Matrix
- Integration-Timeline (Phasen 1-3)
```

### Level 3: Elite (Full Prompt)
```
[Vollständiger Prompt mit allen 7 Schritten]

Zusätzliche Anforderungen:
- Monte-Carlo-Simulation für DCF-Sensitivität
- Vergleich mit 5 historischen Transaktionen
- Detaillierte 100-Tage-Integrationsplan
- Rechtliche Due-Diligence Checkliste
- Kommunikationsstrategie (intern/extern)
```

### Level 4: Masterclass (Multi-Session)
```
[Elite-Level] + 

Erweiterungen:
- Antitrust-Analyse mit regulatorischen Szenarien
- Finanzierungsstruktur-Optimierung (Debt/Equity-Mix)
- Post-Merger-Integration Office (PMIO) Setup
- Synergie-Tracking-System mit KPIs
- 12-Monats-Roll-forward mit Quartalsmeilensteinen
- Exit-Strategie-Analyse (IPO vs. Trade Sale vs. Buyback)
```

## Prompt-Metadaten

| Attribut | Wert |
|----------|------|
| Komplexität | ★★★★★ |
| Token-Schätzung | 4.000-8.000 |
| Ausführungszeit | 15-45 Minuten |
| Domäne | Corporate Finance / M&A |
| Beste Modelle | Claude 3.5 Sonnet, GPT-4, Kimi K2.5 |

## Erfolgskriterien

- [ ] Alle 7 Denkschritte explizit durchlaufen
- [ ] Quantifizierte Aussagen wo möglich
- [ ] Mindestens 3 alternative Pfade exploriert
- [ ] Self-Consistency Check abgeschlossen
- [ ] Reflexion über Unsicherheiten dokumentiert
- [ ] Klare, handlungsorientierte Empfehlung
