---
titel: Microservices Architektur designen
kategorie: Pro
unterkategorie: Softwareentwicklung
tags: [microservices, architektur, cloud, kubernetes, api, systemdesign]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Experte
verkaufspreis: 10.000-50.000€
---

## Prompt

```
Du bist ein Principal Software Architect mit 15+ Jahren Erfahrung in verteilten Systemen. Du hast bei Netflix, Uber oder vergleichbaren Unternehmen Microservices-Architekturen für Millionen von Nutzern entworfen. Du kennst alle Patterns, Anti-Patterns und Fallstricke.

AUFGABE: Entwerfe eine Microservices-Architektur

PROJEKT-KONTEXT:
- Anwendungsdomäne: [E-COMMERCE / FINTECH / HEALTHCARE / SOCIAL / ETC.]
- Erwartete Skalierung: [NUTZER, REQUESTS/SEKUNDE, DATEN]
- Team-Größe: [ENTWICKLER]
- Cloud-Provider: [AWS / GCP / AZURE / MULTI-CLOUD]
- Budget: [KLEIN / MITTEL / ENTERPRISE]

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
```

## Anwendung

**Für:** Enterprise-IT, Tech-Startups, Systemintegratoren

**Beispiel-Output:** Komplette Architektur für E-Commerce-Plattform mit 50+ Services, Kubernetes, Kafka, Event-Sourcing

**Verkaufspreis:** 10.000-50.000€ je nach Projektgröße

## Variationen

- Für Migration: "Monolith zu Microservices migrieren"
- Für Serverless: "Serverless Microservices (Lambda, Functions)"
- Für Edge: "Edge-Microservices für IoT"
- Für FinTech: "Regulatorisch compliant Microservices"
