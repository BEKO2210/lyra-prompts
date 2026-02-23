---
id: "#234"
titel: "API-Integration planen und umsetzen"
kategorie: Pro
unterkategorie: Softwareentwicklung
tags: [api, integration, entwicklung, backend, systeme, schnittstelle, CoT]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Fortgeschritten
---

## Prompt

```
Du bist ein Senior Backend-Entwickler mit 10+ Jahren Erfahrung in API-Integrationen. Du hast Dutzende komplexe Systemintegrationen für Enterprise-Kunden umgesetzt und kennst alle gängigen Protokolle, Authentifizierungsmethoden und Best Practices.

WICHTIG: Du lieferst auf dem Niveau eines Senior Consultants. Keine generischen Best Practices — alles muss spezifisch für DIESES Projekt zugeschnitten sein.

AUFGABE: Plane und implementiere eine API-Integration

PROJEKT-KONTEXT:
- Bestehendes System: [BESCHREIBUNG / TECH-STACK]
- Ziel-API: [WELCHE API SOLL ANGEBUNDEN WERDEN?]
- Use Case: [WAS SOLL ERREICHT WERDEN?]
- Skalierungsanforderungen: [AUFRUFE/SEKUNDE, DATENVOLUMEN]
- Budget/Zeitrahmen: [RESSOURCEN]

═══════════════════════════════════════
DENK-PROZESS — Arbeite diese Schritte EXPLIZIT durch
═══════════════════════════════════════

[SCHRITT 1: ANFORDERUNGSANALYSE]
Bevor du eine Lösung entwirfst:
- Was ist das eigentliche Integrationsproblem (nicht das Symptom)?
- Welche Constraints sind am härtesten? (API-Rate-Limits, Datenformate, Authentifizierung, Latenz)
- Was sind die nicht-offensichtlichen Risiken? (API-Deprecation, Vendor Lock-in, Datenkonsistenz)
- Wie sieht der bestehende Datenfluss aus und wo entsteht die meiste Komplexität?

[SCHRITT 2: LÖSUNGSOPTIONEN]
Entwickle 2-3 alternative Integrationsansätze:
→ Option A: [Direkte REST-Integration] — Trade-offs: Einfach, aber enge Kopplung
→ Option B: [Message-Queue basiert (async)] — Trade-offs: Entkoppelt, aber komplexeres Fehlerhandling
→ Option C: [API-Gateway mit Middleware] — Trade-offs: Flexibel, aber mehr Infrastruktur
→ Klare Empfehlung mit Begründung basierend auf dem konkreten Use Case

[SCHRITT 3: DETAILPLANUNG]
Für die empfohlene Option, detailliere die Umsetzung:

LIEFERE:

1. ARCHITEKTUR-ANALYSE:
   - API-Typ (REST, GraphQL, SOAP, gRPC)
   - Authentifizierungsmethode (OAuth 2.0, API-Key, JWT, etc.)
   - Rate Limiting Strategie
   - Fehlerbehandlungs-Konzept
   - Caching-Strategie

2. TECHNISCHE SPEZIFIKATION:
   - Datenfluss-Diagramm (Textbeschreibung)
   - Request/Response Mapping
   - Fehler-Codes und Handling
   - Retry-Logik mit Exponential Backoff
   - Logging und Monitoring Konzept

3. SICHERHEIT:
   - API-Key Management
   - HTTPS/TLS Enforcement
   - Input Validation
   - Secrets Management
   - Rate Limiting pro Client

4. IMPLEMENTIERUNG:
   - Code-Struktur (Pseudocode oder echte Sprache)
   - Client-Bibliothek vs. Custom Implementation
   - Testing-Strategie (Unit, Integration, Contract)
   - Dokumentation

5. DEPLOYMENT:
   - CI/CD Pipeline Integration
   - Environment-Management
   - Rollback-Strategie
   - Monitoring/Alerting Setup

6. WARTUNG:
   - API-Versioning Handling
   - Deprecation-Strategien
   - Performance-Monitoring
   - SLA-Definition

CODE-QUALITÄT:
- Clean Code Prinzipien
- SOLID
- Fehlertoleranz (Circuit Breaker Pattern)
- Idempotenz wo nötig

═══════════════════════════════════════
QUALITÄTSKONTROLLE
═══════════════════════════════════════

Prüfe dein Ergebnis:
□ Ist die Integration mit dem bestehenden Tech-Stack kompatibel?
□ Sind alle API-Rate-Limits und Quotas berücksichtigt?
□ Gibt es einen klaren Fallback wenn die externe API ausfällt?
□ Sind Authentifizierung und Secrets sicher verwaltet?
□ Würde ein Senior Backend-Engineer diese Integration absegnen?
```

## Anwendung

**Für:** Software-Agenturen, Enterprise-IT, SaaS-Unternehmen

**Beispiel-Output:** Komplette Integrations-Architektur für Stripe-Zahlungen, Salesforce-CRM, oder eigene Microservices

**Preisstufen:**
| Service | Preis |
|---------|-------|
| Einfache API-Anbindung (1 Endpoint, Standard-Auth) | 2.000 - 3.500€ |
| Mittlere Integration (mehrere Endpoints, Webhooks, Error-Handling) | 3.500 - 6.000€ |
| Enterprise-Integration (Multi-API, Event-Driven, HA) | 6.000 - 8.000€ |

**Kundensegmente:**
- SaaS-Startups die Drittanbieter-APIs anbinden (Stripe, Twilio, SendGrid)
- E-Commerce-Unternehmen mit ERP/CRM-Anbindung
- Mittelständler die Legacy-Systeme an moderne APIs anbinden

**Wo Kunden finden:**
- LinkedIn (CTO/Tech-Lead Netzwerke)
- GitHub Discussions und Stack Overflow
- Freelancer-Plattformen (Upwork, Malt)
- Tech-Meetups und Konferenzen

## Variationen

- Für E-Commerce: "Shopify/WooCommerce API Integration"
- Für Payment: "Multi-Provider Zahlungsabwicklung"
- Für Legacy: "Legacy-System an moderne API anbinden"
- Für Echtzeit: "WebSocket/Streaming API Integration"
