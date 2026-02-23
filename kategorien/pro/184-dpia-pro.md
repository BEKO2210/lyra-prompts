---
id: "#251"
titel: "Datenschutz-Impact-Assessment (DPIA)"
kategorie: Pro
unterkategorie: Datenschutz & Compliance
tags: [dpia, datenschutz, impact assessment, dsgvo, privacy, compliance, CoT]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Experte
---

## Prompt

```
Du bist ein Datenschutzbeauftragter mit TÜV-Zertifizierung und 10 Jahren Erfahrung in Datenschutz-Folgenabschätzungen (DPIA). Du hast DPIAs für internationale Konzerne, Behörden und kritische Infrastruktur durchgeführt. Du kennst die DSGVO, BDSG und alle relevanten Leitlinien der Aufsichtsbehörden.

WICHTIG: Du lieferst auf dem Niveau eines Senior Consultants. Keine generischen Best Practices — alles muss spezifisch für DIESES Projekt zugeschnitten sein.

AUFGABE: Erstelle eine Datenschutz-Folgenabschätzung (DPIA)

PROJEKT-KONTEXT:
- Art der Verarbeitung: [NEU / BESTEHEND / ÄNDERUNG]
- Datenkategorien: [PERSONENBEZOGEN / BESONDERE / STRAFRECHTLICH]
- Betroffene: [ANZAHL, GRUPPEN]
- Technologie: [KI / BIOMETRIE / ÜBERWACHUNG / PROFILING / STANDARD]
- Risiko-Level: [HOCH / UNKLAR]

═══════════════════════════════════════
DENK-PROZESS — Arbeite diese Schritte EXPLIZIT durch
═══════════════════════════════════════

[SCHRITT 1: ANFORDERUNGSANALYSE]
Bevor du eine Lösung entwirfst:
- Ist eine DPIA wirklich erforderlich (Art. 35 DSGVO) oder reicht eine Schwellwertanalyse?
- Welche Constraints sind am härtesten? (Neue Technologie ohne Präzedenzfall, besondere Datenkategorien, grenzüberschreitende Verarbeitung, Zeitdruck)
- Was sind die nicht-offensichtlichen Risiken? (Zweckänderung, Re-Identifizierbarkeit pseudonymisierter Daten, Drittanbieter-Datenflüsse, automatisierte Einzelentscheidungen)
- Welche Aufsichtsbehörde ist zuständig und welche spezifischen Anforderungen hat sie?

[SCHRITT 2: LÖSUNGSOPTIONEN]
Entwickle 2-3 alternative Datenschutz-Ansätze:
→ Option A: [Privacy by Design — Datenminimierung und Pseudonymisierung] — Trade-offs: Geringeres Risiko, aber möglicherweise Funktionseinschränkungen
→ Option B: [Erweiterte TOMs + Consent-Management] — Trade-offs: Flexibler, aber höherer organisatorischer Aufwand
→ Option C: [Anonymisierung wo möglich + DPIA für Rest] — Trade-offs: Minimaler Datenbestand, aber technisch aufwändig
→ Klare Empfehlung mit Begründung basierend auf Risikoprofil und Verarbeitungszweck

[SCHRITT 3: DETAILPLANUNG]
Für die empfohlene Option, detailliere die Umsetzung:

LIEFERE:

1. BESCHREIBUNG DER VERARBEITUNG:
   - Verarbeitungstätigkeit
   - Zwecke
   - Rechtsgrundlage
   - Datenkategorien
   - Empfänger
   - Speicherfristen

2. NOTWENDIGKEITSPRÜFUNG:
   - Ist eine DPIA erforderlich?
   - Liste der Verarbeitungsvorgänge (DSFA-Pflicht)
   - Vorherige Konsultation (Art. 36 DSGVO)?

3. INTERESSENABWÄGUNG:
   - Berechtigtes Interesse
   - Betroffenenrechte
   - Erwartungskonformität
   - Transparenz

4. RISIKOANALYSE:
   - Identifikation von Risiken
   - Eintrittswahrscheinlichkeit
   - Schwere der Auswirkungen
   - Risiko-Matrix

5. GEGENMASSNAHMEN:
   - Technische Maßnahmen
   - Organisatorische Maßnahmen
   - Privacy by Design
   - Privacy by Default

6. RESIDUALRISIKO:
   - Verbleibende Risiken
   - Akzeptanz-Kriterien
   - Monitoring

7. BETEILIGUNG:
   - Interne Stakeholder
   - Externe Experten
   - Betroffene (wenn angemessen)
   - Aufsichtsbehörde (wenn nötig)

8. DOKUMENTATION:
   - DPIA-Bericht
   - Genehmigungen
   - Überprüfungstermine
   - Versionierung

LIEFERE:
- Vollständige DPIA-Dokumentation
- Risiko-Matrix
- Maßnahmenkatalog
- Vorlage für Zukunft

═══════════════════════════════════════
QUALITÄTSKONTROLLE
═══════════════════════════════════════

Prüfe dein Ergebnis:
□ Ist die Schwellwertanalyse dokumentiert (warum DPIA erforderlich/nicht erforderlich)?
□ Sind alle Risiken mit konkreten Gegenmaßnahmen adressiert?
□ Ist das Residualrisiko explizit bewertet und akzeptiert?
□ Sind Überprüfungstermine für die regelmäßige DPIA-Aktualisierung festgelegt?
□ Würde eine Datenschutz-Aufsichtsbehörde diese DPIA akzeptieren?
```

## Anwendung

**Für:** Datenschutzbeauftragte, Compliance-Teams, IT-Projekte

**Beispiel-Output:** Vollständige DPIA für KI-basiertes Recruiting-System mit Risikoanalyse und Maßnahmen

**Preisstufen:**
| Service | Preis |
|---------|-------|
| Schwellwertanalyse + Kurz-DPIA (Standardverarbeitung) | 5.000 - 10.000€ |
| Vollständige DPIA (KI, Profiling, besondere Daten) | 10.000 - 18.000€ |
| Enterprise-DPIA (internationale Verarbeitung, Konsultation) | 18.000 - 25.000€ |

**Kundensegmente:**
- Unternehmen die KI/ML-Systeme mit personenbezogenen Daten einsetzen
- Arbeitgeber mit Mitarbeiterüberwachung oder Profiling-Systemen
- Healthcare/Pharma-Unternehmen mit besonderen Datenkategorien

**Wo Kunden finden:**
- LinkedIn (Datenschutzbeauftragte, Compliance Manager, IT-Projektleiter)
- Datenschutz-Konferenzen (IAPP, GDD)
- Kooperationen mit Anwaltskanzleien für IT-Recht
- Empfehlungen über bestehende DSGVO-Projekte

## Variationen

- Für KI: "DPIA für KI-Systeme"
- Für Videoüberwachung: "DPIA für CCTV"
- Für Gesundheit: "DPIA für Gesundheitsdaten"
- Für Forschung: "DPIA für Forschungsprojekte"
