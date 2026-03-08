---
titel: "Code-Review durchführen"
kategorie: Technik
unterkategorie: Softwareentwicklung
tags: [code-review, entwicklung, qualität, best-practices]
erstellt: 2026-02-23
plattformen: [ChatGPT, Claude]
---

# Code-Review durchführen

## Prompt
```
Rolle: Senior-Entwickler und Code-Review-Experte
Kontext: Ich möchte folgenden Code reviewen: [CODE EINFÜGEN]
Sprache/Framework: [PYTHON/JAVASCRIPT/GO/etc.]
Kontext: [TEIL EINES PROJEKTS/STANDALONE]
Mein Erfahrungslevel: [JUNIOR/MID/SENIOR]
Aufgabe: Führe ein strukturiertes Code-Review durch
Einschränkungen:
- Priorisiere Sicherheit, Performance, Wartbarkeit
- Erkläre Warum, nicht nur Was
- Schlage konkrete Alternativen vor
Ausgabe: Bewertung nach Kategorien (Lesbarkeit, Effizienz, Sicherheit, Testing), gefundene Issues mit Schweregrad, konkrete Verbesserungsvorschläge, positive Aspekte, Lernressourcen
```

## Anwendung
**Input:**
- Code: Python-Funktion für Datei-Upload
- Sprache: Python 3.11
- Kontext: Web-API Endpoint
- Level: Mid-Level

**Output:** AI analysiert: Input-Validierung fehlt, Race Condition möglich, kein Size-Limit, schlägt vor: try-except, MIME-Type Check, Streaming für große Dateien

## Variationen
- Für Legacy-Code: "Schrittweise Refactoring-Strategie"
- Für Performance-kritischen Code: "Big-O-Analyse und Optimierungspotenzial"
- Für Security-Review: "OWASP-Top-10 Checkliste anwenden"
