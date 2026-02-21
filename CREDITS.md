# Lyra Prompts - Credits & Changelog

## Über dieses Repository

Lyra Prompts ist eine kuratierte Sammlung von AI-Prompts nach der 4-D Methodology (Rolle, Kontext, Aufgabe, Ausgabe).

## Ersteller

**Belkis Aslani** (BEKO2210)
- GitHub: https://github.com/BEKO2210
- Portfolio: https://BEKO2210.github.io/My-table-of-contents-

## Mitwirkende

| Name | Beitrag | Datum |
|------|---------|-------|
| **Belkis** | Initiales Setup, 50+ Bild-Prompts, 30+ Text-Prompts | 2026-02-20 |
| **Claude Code** (Anthropic) | 5 PRO Business-Prompts, 5 Human-Animal Hybrid Bild-Prompts, Template-System | 2026-02-21 |
| **Belkis v2** (Kimi K2.5) | 15 Prompts (10min Batch), 9 Prompts (10min Batch), Auto-Memory-System | 2026-02-21 |

## Changelog

### 2026-02-21
- **Template-System hinzugefügt** (`template/` Ordner)
  - `TEMPLATE.md` für Text-Prompts
  - `TEMPLATE-BILD.md` für Bild-Prompts
  - `README.md` mit Anleitung
  - Beispiele für Alltag und Bild
- **15 neue Prompts** (Belkis v2, 10min Batch)
  - Alle 9 Kategorien abgedeckt
  - Wocheneinkauf, Morgenroutine, Karriereziele, etc.
- **9 neue Prompts** (Belkis v2, 10min Batch)
  - Wochenplanung, Haushaltsbudget, etc.
- **5 PRO Prompts** (Claude Code)
  - Business-Strategie, Verhandlungsstrategie, KI-Architektur, Finanzmodell, Executive Briefing
- **5 Bild-Prompts** (Claude Code)
  - Human-Animal Hybrids: Löwe, Wolf, Adler, Schlange, Hirsch
- **Auto-Memory-System** implementiert (Belkis v2)
  - Automatische Persistenz alle 10 Minuten
  - `.secrets/` für API-Keys
  - Cron-Job für Memory-Flush

### 2026-02-20
- **Initiales Release**
  - 50 Bild-Prompts (Visualisierung & Transformation)
  - 30+ Text-Prompts (Alltag, Beruf, Lernen, etc.)
  - 9 Kategorien
  - HTML-Interface mit Suche und Filter

## Prompt-Statistik

| Kategorie | Anzahl |
|-----------|--------|
| Alltag & Leben | ~15 |
| Beruf & Karriere | ~12 |
| Lernen & Wachstum | ~10 |
| Kommunikation & Beziehungen | ~10 |
| Kreativität & Freizeit | ~8 |
| Gesundheit & Wohlbefinden | ~10 |
| Technik & Alltag | ~8 |
| Spezielle Situationen | ~7 |
| Bildbearbeitung & KI-Visualisierung | ~55 |
| PRO (PIN-geschützt) | ~10 |
| **Gesamt** | **~165** |

## Doppelte entfernt

| Prompt | Ursprünglich in | Entfernt aus | Grund |
|--------|-----------------|--------------|-------|
| Schwieriges Gespräch vorbereiten | Beruf & Karriere (Original) | Kommunikation & Beziehungen (Duplikat) | Original behalten |

## Tools verwendet

- **Claude Code** (Anthropic) - Prompt-Generierung, Code-Review
- **Kimi K2.5** (Moonshot AI) - Batch-Prompt-Generierung, Memory-System
- **GitHub** - Repository-Hosting
- **GitHub Pages** - Live-Deployment

## Lizenz

MIT License - Siehe LICENSE Datei

---

*Letzte Aktualisierung: 2026-02-21*
