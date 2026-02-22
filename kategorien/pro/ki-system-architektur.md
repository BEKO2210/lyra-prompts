---
id: "#187"
titel: KI-System Architektur designen
kategorie: Pro
unterkategorie: Technologie & KI
tags: [ki, architektur, systemdesign, llm, enterprise]
erstellt: 2026-02-21
plattformen: [ChatGPT, Claude]
---

# KI-System Architektur designen

## Prompt

```
Rolle: Principal AI Architect (ehemals bei OpenAI/Anthropic/Google DeepMind)
Kontext: Ich muss ein KI-System designen für folgenden Use Case:
Business-Problem: [WAS SOLL GELÖST WERDEN?]
Aktueller Prozess: [WIE WIRD ES HEUTE GEMACHT?]
Skalierungsanforderungen:
- Nutzer: [ANZAHL gleichzeitig/Tag/Monat]
- Latenz-Anforderung: [MAXIMALE ANTWORTZEIT]
- Durchsatz: [ANFRAGEN/SEKUNDE]
Datenlage:
- Vorhandene Daten: [MENGE, QUALITÄT, STRUKTUR]
- Daten-Sensitivität: [ÖFFENTLICH / INTERN / VERTRAULICH / GEHEIM]
- Compliance: [GDPR, HIPAA, SOX, etc.]
Budget-Rahmen: [KAPITAL + LAUFENDE KOSTEN]
Team-Kapazitäten: [INTERNE DEVS, ML-ENGINEERS, DATA SCIENTISTS]
Integration: [BESTEHENDE SYSTEME, APIs, Datenbanken]
Aufgabe: Designe eine produktionsreife KI-Architektur
Einschränkungen:
- Vendor-Lock-in minimieren wo möglich
- Kosten-Effizienz bei Skalierung
- Observability & Debugging eingebaut
- Disaster Recovery Plan
Ausgabe:
1. Architektur-Übersicht (Diagramm-Beschreibung)
2. Komponenten-Stack:
   - LLM/Modell-Auswahl (mit Begründung)
   - Hosting (Cloud vs. On-Prem vs. Hybrid)
   - Vector Database
   - Caching-Layer
   - Monitoring & Logging
3. Datenfluss (Request → Response Pipeline)
4. Sicherheitsarchitektur:
   - Prompt Injection Prevention
   - Data Leakage Protection
   - Access Control
5. Kostenmodell:
   - Setup-Kosten
   - Laufende Kosten (pro 1k Anfragen)
   - Break-Even-Analyse
6. Implementierungs-Roadmap (MVP → Production)
7. Risk Assessment & Mitigation
8. Alternativen-Vergleich (3 Optionen: Budget, Balanced, Premium)
```

## Anwendung

**Für:** CTOs, AI-Teams, Enterprise Architecture

**Input:** "Kundenservice-Chatbot, 10k Anfragen/Tag, <2s Latenz, GDPR-konform, €50k Budget"

**Output:** Produktionsreife Architektur-Dokumentation

## Variationen

- Für RAG-Systeme: "Knowledge Base Architecture"
- Für Agenten: "Multi-Agent System Design"
- Für Bildverarbeitung: "Computer Vision Pipeline"
- Für Echtzeit: "Streaming Inference Architecture"
