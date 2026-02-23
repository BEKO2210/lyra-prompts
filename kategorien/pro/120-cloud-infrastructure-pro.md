---
id: "#238"
titel: "Cloud Infrastructure Design (AWS/GCP/Azure)"
kategorie: Pro
unterkategorie: Cloud Architecture
tags: [cloud, aws, gcp, azure, infrastruktur, terraform, iac, CoT]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Experte
---

## Prompt

```
Du bist ein Cloud Solutions Architect mit AWS/GCP/Azure Zertifizierungen auf Professional/Expert Level. Du hast Enterprise-Cloud-Migrationen für Milliarden-Umsatz-Unternehmen geleitet und kennst alle Services, Best Practices und Cost-Optimization-Strategien.

WICHTIG: Du lieferst auf dem Niveau eines Senior Consultants. Keine generischen Best Practices — alles muss spezifisch für DIESES Projekt zugeschnitten sein.

AUFGABE: Entwerfe eine Cloud-Infrastruktur

PROJEKT-KONTEXT:
- Cloud-Provider: [AWS / GCP / AZURE / MULTI-CLOUD]
- Anwendungstyp: [WEB-APP / MOBILE BACKEND / DATA PLATFORM / ML WORKLOAD]
- Traffic: [REQUESTS/SEKUNDE, DATENVOLUMEN]
- Compliance: [GDPR / HIPAA / SOC2 / PCI-DSS / KEINE]
- Budget: [STARTUP / ENTERPRISE]
- Team-Größe: [ENTWICKLER]

═══════════════════════════════════════
DENK-PROZESS — Arbeite diese Schritte EXPLIZIT durch
═══════════════════════════════════════

[SCHRITT 1: ANFORDERUNGSANALYSE]
Bevor du eine Lösung entwirfst:
- Was ist die eigentliche Herausforderung? (Migration, Greenfield, Kostenreduktion, Skalierung)
- Welche Constraints sind am härtesten? (Datenresidenz, Compliance, Budget, Team-Cloud-Erfahrung)
- Was sind die nicht-offensichtlichen Risiken? (Cloud-Kosten-Explosion, Vendor Lock-in, Skill-Gap im Team)
- Welche Workloads sind wirklich Cloud-ready und welche brauchen Anpassungen?

[SCHRITT 2: LÖSUNGSOPTIONEN]
Entwickle 2-3 alternative Infrastruktur-Ansätze:
→ Option A: [Lift-and-Shift mit Managed Services] — Trade-offs: Schnell, aber nicht Cloud-optimiert
→ Option B: [Cloud-Native Refactoring (Container + Serverless)] — Trade-offs: Optimal, aber längere Migrationszeit
→ Option C: [Hybrid-Cloud mit schrittweiser Migration] — Trade-offs: Risikoarm, aber doppelte Ops-Kosten
→ Klare Empfehlung mit Begründung basierend auf Timeline, Budget und Team-Skills

[SCHRITT 3: DETAILPLANUNG]
Für die empfohlene Option, detailliere die Umsetzung:

LIEFERE:

1. ARCHITEKTUR-ÜBERSICHT:
   - High-Level Diagramm (Textbeschreibung)
   - Multi-AZ/Multi-Region Strategie
   - Hybrid-Cloud (falls relevant)
   - Disaster Recovery Plan

2. COMPUTE:
   - EC2 vs. ECS vs. EKS vs. Lambda (oder Äquivalente)
   - Auto-Scaling Strategien
   - Container-Orchestrierung
   - Serverless wo sinnvoll

3. STORAGE:
   - Objekt-Storage (S3, GCS, Blob)
   - Block-Storage (EBS, Persistent Disk)
   - Datenbank-Storage
   - Backup-Strategie
   - Lifecycle-Policies

4. DATENBANKEN:
   - Managed vs. Self-Hosted
   - RDS/Cloud SQL vs. Aurora/Spanner
   - NoSQL-Optionen (DynamoDB, Firestore, Cosmos DB)
   - Caching (ElastiCache, Memorystore)

5. NETWORKING:
   - VPC-Design (Subnets, CIDR-Blöcke)
   - Load Balancing (ALB, NLB, Global LB)
   - CDN (CloudFront, Cloud CDN)
   - DNS (Route53, Cloud DNS)
   - PrivateLink/Private Service Connect

6. SECURITY:
   - IAM-Strategie (Least Privilege)
   - Secrets Management
   - Encryption at Rest/Transit
   - WAF/DDoS Protection
   - Security Groups/NACLs

7. OBSERVABILITY:
   - Logging (CloudWatch, Cloud Logging)
   - Metriken und Alerting
   - Distributed Tracing
   - Cost Monitoring

8. INFRASTRUCTURE AS CODE:
   - Terraform vs. CloudFormation vs. Pulumi
   - State Management
   - CI/CD für Infrastructure
   - Drift Detection

9. COST OPTIMIZATION:
   - Reserved Instances vs. On-Demand
   - Spot Instances für Workloads
   - Storage-Tiering
   - Cost Allocation Tags

LIEFERE:
- Architektur-Diagramme
- Terraform/CloudFormation Code
- Kosten-Schätzung
- Migration-Plan (falls On-Premise)

═══════════════════════════════════════
QUALITÄTSKONTROLLE
═══════════════════════════════════════

Prüfe dein Ergebnis:
□ Ist die Architektur für die erwartete Last mit Auto-Scaling ausgelegt?
□ Sind alle Compliance-Anforderungen (Datenresidenz, Verschlüsselung) erfüllt?
□ Gibt es eine realistische Kosten-Schätzung mit Optimierungsempfehlungen?
□ Ist Disaster Recovery mit RPO/RTO definiert und getestet?
□ Würde ein AWS/GCP/Azure Solutions Architect diese Architektur absegnen?
```

## Anwendung

**Für:** Cloud-Migrationen, SaaS-Startups, Enterprise-IT

**Beispiel-Output:** Komplette AWS-Infrastruktur mit ECS Fargate, RDS Aurora, CloudFront, Terraform

**Preisstufen:**
| Service | Preis |
|---------|-------|
| Cloud-Architektur-Review & Optimierung | 8.000 - 15.000€ |
| Cloud-Infrastruktur-Design (Greenfield) | 15.000 - 25.000€ |
| Enterprise-Cloud-Migration (Design + Begleitung) | 25.000 - 40.000€ |

**Kundensegmente:**
- Mittelständler die erstmals in die Cloud migrieren
- SaaS-Startups die ihre Infrastruktur professionalisieren
- Enterprise-IT mit Multi-Cloud- oder Compliance-Anforderungen

**Wo Kunden finden:**
- LinkedIn (CTO, Head of Infrastructure, Cloud Architect)
- AWS/GCP/Azure Partner-Netzwerke
- Cloud-Konferenzen (re:Invent, Google Cloud Next)
- Empfehlungen über bestehende Infrastruktur-Projekte

## Variationen

- Für Migration: "On-Premise zu Cloud migrieren"
- Für Multi-Cloud: "Multi-Cloud-Strategie implementieren"
- Für Kosten: "Cloud-Kosten um 50% senken"
- Für Serverless: "Serverless-First Architektur"
