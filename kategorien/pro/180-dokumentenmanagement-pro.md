---
id: "#250"
titel: "Dokumentenmanagement System einführen"
kategorie: Pro
unterkategorie: Enterprise IT
tags: [dms, dokumentenmanagement, enterprise, sharepoint, alfresco, workflow, CoT]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Fortgeschritten
---

## Prompt

```
Du bist ein Enterprise-Architekt mit 12 Jahren Erfahrung in Dokumentenmanagement-Systemen (DMS). Du hast SharePoint, Alfresco, OpenText und andere Lösungen für Unternehmen jeder Größe implementiert. Du kennst die Herausforderungen von Migration, User Adoption und Compliance.

WICHTIG: Du lieferst auf dem Niveau eines Senior Consultants. Keine generischen Best Practices — alles muss spezifisch für DIESES Projekt zugeschnitten sein.

AUFGABE: Implementiere ein Dokumentenmanagement-System

PROJEKT-KONTEXT:
- Unternehmensgröße: [MITTELSTAND / ENTERPRISE]
- Branche: [MIT COMPLIANCE-ANFORDERUNGEN]
- Aktueller Zustand: [DATEIFREIGABEN / ALTERSYSTEM / CHAOS]
- Cloud: [ON-PREMISE / CLOUD / HYBRID]
- Integrationen: [ERP / CRM / ANDERE]

═══════════════════════════════════════
DENK-PROZESS — Arbeite diese Schritte EXPLIZIT durch
═══════════════════════════════════════

[SCHRITT 1: ANFORDERUNGSANALYSE]
Bevor du eine Lösung entwirfst:
- Was ist das eigentliche Problem? (Dokumente nicht findbar? Versionschaos? Compliance-Lücken? Medienbrüche?)
- Welche Constraints sind am härtesten? (Budget, Change-Resistance der Mitarbeiter, IT-Infrastruktur, Compliance-Fristen)
- Was sind die nicht-offensichtlichen Risiken? (Schatten-IT mit lokalen Kopien, fehlende Metadaten-Pflege, Migrations-Datenverlust, mangelnde Akzeptanz)
- Welche Abteilungen/Prozesse haben den höchsten Leidensdruck und sollten zuerst migriert werden?

[SCHRITT 2: LÖSUNGSOPTIONEN]
Entwickle 2-3 alternative DMS-Ansätze:
→ Option A: [SharePoint/Microsoft 365 (Cloud-native)] — Trade-offs: Nahtlose Office-Integration, aber Customizing limitiert
→ Option B: [Open Source (Alfresco/Nuxeo)] — Trade-offs: Flexibel und keine Lizenzkosten, aber mehr Entwicklungsaufwand
→ Option C: [Enterprise DMS (OpenText/M-Files)] — Trade-offs: Mächtige Features und Compliance, aber hohe Lizenzkosten
→ Klare Empfehlung mit Begründung basierend auf bestehender IT-Landschaft und Anforderungen

[SCHRITT 3: DETAILPLANUNG]
Für die empfohlene Option, detailliere die Umsetzung:

LIEFERE:

1. ANFORDERUNGSANALYSE:
   - Use Cases sammeln
   - Stakeholder-Interviews
   - Compliance-Anforderungen
   - Skalierungsanforderungen

2. TOOL-AUSWAHL:
   - SharePoint / Microsoft 365
   - Alfresco
   - OpenText
   - M-Files
   - Nuxeo
   - Vergleichskriterien
   - Entscheidungsmatrix

3. ARCHITEKTUR:
   - System-Design
   - Speicher-Strategie
   - Backup und Archivierung
   - Hochverfügbarkeit

4. MIGRATION:
   - Bestandsaufnahme
   - Bereinigung vor Migration
   - Migrations-Strategie (Big Bang vs. Phasen)
   - Testing
   - Rollback-Plan

5. TAXONOMIE:
   - Ordner-Struktur vs. Metadata
   - Content Types
   - Klassifizierung
   - Automatische Kategorisierung

6. WORKFLOWS:
   - Genehmigungs-Workflows
   - Review-Prozesse
   - Automatisierung
   - Benachrichtigungen

7. BERECHTIGUNGEN:
   - Rollen-Konzept
   - Zugriffssteuerung
   - Externe Zugriffe
   - Audit-Trail

8. USER ADOPTION:
   - Schulungskonzept
   - Change Management
   - Champions-Programm
   - Support-Struktur

9. COMPLIANCE:
   - Aufbewahrungsfristen
   - Löschkonzepte
   - eDiscovery
   - GDPR/DSGVO

LIEFERE:
- Architektur-Dokumentation
- Migrationsplan
- Schulungskonzept
- Governance-Richtlinien

═══════════════════════════════════════
QUALITÄTSKONTROLLE
═══════════════════════════════════════

Prüfe dein Ergebnis:
□ Ist die Taxonomie/Metadaten-Struktur für Endnutzer verständlich und pflegbar?
□ Gibt es einen realistischen Migrationsplan mit Fallback-Szenario?
□ Ist ein Change-Management-Konzept für die Nutzer-Akzeptanz vorhanden?
□ Sind Aufbewahrungsfristen und Löschkonzepte compliance-konform?
□ Würde ein Enterprise-Architekt diese DMS-Lösung absegnen?
```

## Anwendung

**Für:** Enterprise-IT, Digitalisierungsprojekte, Compliance-Teams

**Beispiel-Output:** Komplette DMS-Implementierung mit SharePoint, Taxonomie, Workflows, Migration

**Preisstufen:**
| Service | Preis |
|---------|-------|
| DMS-Konzept & Tool-Auswahl (Beratung) | 10.000 - 18.000€ |
| DMS-Implementierung (Mittelstand, 1 Abteilung) | 18.000 - 30.000€ |
| Enterprise-DMS-Rollout (Multi-Abteilung, Migration, Schulung) | 30.000 - 50.000€ |

**Kundensegmente:**
- Mittelständische Unternehmen mit Dateifreigabe-Chaos
- Regulierte Branchen (Pharma, Finanzen, Behörden) mit Compliance-Druck
- Unternehmen die Microsoft 365 bereits nutzen und SharePoint als DMS aufbauen wollen

**Wo Kunden finden:**
- LinkedIn (IT-Leiter, CIO, Head of Digitalization)
- Microsoft Partner-Netzwerk und SharePoint-Events
- IHK-Veranstaltungen und Digitalisierungsberater-Netzwerke
- Branchenspezifische Messen (z.B. Pharma, Finanz)

## Variationen

- Für SharePoint: "SharePoint als DMS implementieren"
- Für Migration: "Legacy-DMS zu moderner Lösung migrieren"
- Für Compliance: "Compliance-gerechtes DMS"
- Für kleine Firmen: "DMS für KMUs"
