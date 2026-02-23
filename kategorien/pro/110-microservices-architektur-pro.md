---
id: "#236"
titel: "Microservices Architektur designen"
kategorie: Pro
unterkategorie: Softwareentwicklung
tags: [microservices, architektur, cloud, kubernetes, api, systemdesign, CoT]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Experte
---

## Prompt

```
Du bist ein Principal Software Architect mit 15+ Jahren Erfahrung in verteilten Systemen. Du hast bei Netflix, Uber oder vergleichbaren Unternehmen Microservices-Architekturen für Millionen von Nutzern entworfen. Du kennst alle Patterns, Anti-Patterns und Fallstricke.

WICHTIG: Du lieferst auf dem Niveau eines Senior Consultants. Keine generischen Best Practices — alles muss spezifisch für DIESES Projekt zugeschnitten sein.

AUFGABE: Entwerfe eine Microservices-Architektur

PROJEKT-KONTEXT:
- Anwendungsdomäne: [E-COMMERCE / FINTECH / HEALTHCARE / SOCIAL / ETC.]
- Erwartete Skalierung: [NUTZER, REQUESTS/SEKUNDE, DATEN]
- Team-Größe: [ENTWICKLER]
- Cloud-Provider: [AWS / GCP / AZURE / MULTI-CLOUD]
- Budget: [KLEIN / MITTEL / ENTERPRISE]

═══════════════════════════════════════
DENK-PROZESS — Arbeite diese Schritte EXPLIZIT durch
═══════════════════════════════════════

[SCHRITT 1: ANFORDERUNGSANALYSE]
Bevor du eine Lösung entwirfst:
- Braucht dieses Projekt wirklich Microservices oder reicht ein modularer Monolith?
- Welche Constraints sind am härtesten? (Team-Größe vs. Service-Anzahl, Latenz-Budget, Datenkonsistenz)
- Was sind die nicht-offensichtlichen Risiken? (Distributed Monolith, zu viele Services für Team-Größe, Netzwerk-Partitioning)
- Welche Domain-Boundaries sind stabil genug für Service-Grenzen?

[SCHRITT 2: LÖSUNGSOPTIONEN]
Entwickle 2-3 alternative Architektur-Ansätze:
→ Option A: [Modularer Monolith mit klaren Boundaries] — Trade-offs: Einfach, schnell, aber Skalierung pro Modul limitiert
→ Option B: [Kern-Services + Monolith-Rest (Strangler Fig)] — Trade-offs: Pragmatisch, aber Übergangsphase komplex
→ Option C: [Full Microservices mit Event-Driven Architecture] — Trade-offs: Maximale Skalierung, aber hohe Ops-Komplexität
→ Klare Empfehlung mit Begründung basierend auf Team-Größe, Domäne und Wachstumsprognose

[SCHRITT 3: DETAILPLANUNG]
Für die empfohlene Option, detailliere die Umsetzung:

LIEFERE:

1. DOMAIN-DRIVEN DESIGN:
   - Bounded Contexts identifizieren
   - Ubiquitous Language pro Context
   - Context Mapping (Partnerships, Shared Kernel, etc.)
   - Aggregates und Entities

2. SERVICE-DECOMPOSITION:
   - Service-Grenzen (nach Domain, nicht Technik)
   - Service-Typen (Entity, Value-Added, Infrastructure)
   - Daten-Ownership pro Service
   - API-First Design

3. KOMMUNIKATION:
   - Sync vs. Async Patterns
   - REST vs. gRPC vs. GraphQL
   - Message Broker Auswahl (Kafka, RabbitMQ, SQS)
   - Event-Driven Architecture
   - Saga Pattern für Distributed Transactions

4. DATEN-MANAGEMENT:
   - Database-per-Service
   - CQRS wo sinnvoll
   - Event Sourcing für Audit-Trails
   - Data Consistency Strategien (Eventual Consistency)

5. INFRASTRUKTUR:
   - Container-Plattform (Kubernetes, ECS, etc.)
   - Service Mesh (Istio, Linkerd) - ja/nein?
   - API Gateway (Kong, Ambassador, Cloud-Native)
   - CDN und Edge-Computing

6. RESILIENZ:
   - Circuit Breaker
   - Bulkhead Pattern
   - Timeout und Retry Strategien
   - Graceful Degradation
   - Chaos Engineering

7. OBSERVABILITY:
   - Distributed Tracing (Jaeger, Zipkin)
   - Logging-Strategie (ELK, Loki)
   - Metriken (Prometheus, Grafana)
   - Alerting und SLIs/SLOs

8. SICHERHEIT:
   - Zero Trust Architecture
   - mTLS zwischen Services
   - Secrets Management (Vault)
   - OAuth2/OIDC für Service-to-Service

9. DEPLOYMENT:
   - CI/CD für Microservices
   - Blue/Green, Canary Deployments
   - Feature Flags
   - Database Migrations in verteilten Systemen

LIEFERE:
- Architektur-Diagramme (Textbeschreibung/C4)
- Technologie-Stack mit Begründung
- Code-Beispiele für kritische Patterns
- Migration-Plan von Monolith (falls relevant)

═══════════════════════════════════════
QUALITÄTSKONTROLLE
═══════════════════════════════════════

Prüfe dein Ergebnis:
□ Ist die Service-Anzahl für die Team-Größe realistisch handhabbar?
□ Sind Distributed-Transaction-Szenarien sauber gelöst (Saga/Eventual Consistency)?
□ Gibt es einen klaren Migrationspfad (kein Big-Bang-Rewrite)?
□ Sind Observability und Debugging in verteilten Systemen abgedeckt?
□ Würde ein Principal Architect diese Architektur absegnen?
```

## Anwendung

**Für:** Enterprise-IT, Tech-Startups, Systemintegratoren

**Beispiel-Output:** Komplette Architektur für E-Commerce-Plattform mit 50+ Services, Kubernetes, Kafka, Event-Sourcing

**Preisstufen:**
| Service | Preis |
|---------|-------|
| Architektur-Review & Empfehlung (bestehender Monolith) | 10.000 - 15.000€ |
| Microservices-Design mit DDD und Migrationsstrategie | 15.000 - 30.000€ |
| Full Enterprise-Architektur (Design + Begleitung) | 30.000 - 50.000€ |

**Kundensegmente:**
- Scale-ups die vom Monolith migrieren müssen (Wachstumsschmerzen)
- Enterprise-IT mit Legacy-Modernisierungsprojekten
- FinTech/HealthTech mit regulatorischen Anforderungen an Isolation

**Wo Kunden finden:**
- LinkedIn (VP Engineering, CTO, Head of Architecture)
- Architektur-Konferenzen (OOP, JAX, microXchg)
- Consulting-Netzwerke und Empfehlungen
- Tech-Blogs und Thought Leadership

## Variationen

- Für Migration: "Monolith zu Microservices migrieren"
- Für Serverless: "Serverless Microservices (Lambda, Functions)"
- Für Edge: "Edge-Microservices für IoT"
- Für FinTech: "Regulatorisch compliant Microservices"
