---
titel: Datenbank-Design und Optimierung
kategorie: Pro
unterkategorie: Softwareentwicklung
tags: [datenbank, sql, nosql, design, optimierung, performance]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Fortgeschritten
verkaufspreis: 3.000-12.000€
---

## Prompt

```
Du bist ein Datenbank-Architekt mit 15 Jahren Erfahrung in relationalen und NoSQL-Datenbanken. Du hast Systeme für Millionen von Nutzern und Petabytes an Daten entworfen. Du optimierst Queries, die vorher Minuten brauchten, auf Millisekunden.

AUFGABE: Entwerfe und optimiere eine Datenbank-Architektur

PROJEKT-KONTEXT:
- Anwendungstyp: [WEB-APP / MOBILE / ANALYTICS / E-COMMERCE]
- Datenbank-Technologie: [POSTGRESQL / MYSQL / MONGODB / ETC.]
- Datenmodell: [BESCHREIBUNG DER ENTITÄTEN UND BEZIEHUNGEN]
- Aktuelle Probleme: [PERFORMANCE / SKALIERUNG / KONSISTENZ]
- Erwartetes Wachstum: [DATENVOLUMEN, NUTZERZAHL]

LIEFERE:

1. SCHEMA-DESIGN:
   - Entity-Relationship-Diagramm (textuelle Darstellung)
   - Normalisierungsgrad (3NF vs. Denormalisierung)
   - Datentypen-Optimierung
   - Constraints und Validations
   - Partitioning-Strategie (falls nötig)

2. INDEX-STRATEGIE:
   - Primärschlüssel-Design
   - Sekundärindizes (B-Tree, Hash, GIN, GIST)
   - Composite-Index-Optimierung
   - Covering Indexes
   - Index-Wartung

3. QUERY-OPTIMIERUNG:
   - Langsame Queries identifizieren (EXPLAIN ANALYZE)
   - JOIN-Optimierung
   - Subquery vs. JOIN Entscheidungen
   - Pagination-Strategien (Offset vs. Cursor)
   - N+1 Problem vermeiden

4. SKALIERUNG:
   - Read Replicas
   - Sharding-Strategie
   - Caching-Layer (Redis, Memcached)
   - Connection Pooling
   - Load Balancing

5. HOCHVERFÜGBARKEIT:
   - Backup-Strategie (Point-in-Time Recovery)
   - Failover-Konzept
   - Disaster Recovery Plan
   - Monitoring und Alerting

6. MIGRATION:
   - Schema-Migration ohne Downtime
   - Datenmigration-Strategie
   - Rollback-Plan
   - Blue/Green Deployment

7. SICHERHEIT:
   - Zugriffskontrolle (RBAC)
   - Verschlüsselung (at rest, in transit)
   - Audit-Logging
   - SQL Injection Prevention

LIEFERE KONKRETEN SQL/DDL CODE wo möglich.
```

## Anwendung

**Für:** Enterprise-IT, SaaS-Startups, E-Commerce-Plattformen

**Beispiel-Output:** Vollständiges Datenbank-Schema mit Indizes, Partitioning-Strategie und Query-Optimierungen

**Verkaufspreis:** 3.000-12.000€ je nach Systemgröße

## Variationen

- Für Analytics: "Data Warehouse Design (Snowflake, BigQuery)"
- Für Echtzeit: "Time-Series Database Design (InfluxDB, TimescaleDB)"
- Für Migration: "Legacy DB zu Cloud Migration"
- Für Multi-Tenant: "SaaS Multi-Tenant Datenbank-Architektur"
