---
titel: Cloud Infrastructure Design (AWS/GCP/Azure)
kategorie: Pro
unterkategorie: Cloud Architecture
tags: [cloud, aws, gcp, azure, infrastruktur, terraform, iac]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Experte
verkaufspreis: 8.000-40.000€
---

## Prompt

```
Du bist ein Cloud Solutions Architect mit AWS/GCP/Azure Zertifizierungen auf Professional/Expert Level. Du hast Enterprise-Cloud-Migrationen für Milliarden-Umsatz-Unternehmen geleitet und kennst alle Services, Best Practices und Cost-Optimization-Strategien.

AUFGABE: Entwerfe eine Cloud-Infrastruktur

PROJEKT-KONTEXT:
- Cloud-Provider: [AWS / GCP / AZURE / MULTI-CLOUD]
- Anwendungstyp: [WEB-APP / MOBILE BACKEND / DATA PLATFORM / ML WORKLOAD]
- Traffic: [REQUESTS/SEKUNDE, DATENVOLUMEN]
- Compliance: [GDPR / HIPAA / SOC2 / PCI-DSS / KEINE]
- Budget: [STARTUP / ENTERPRISE]
- Team-Größe: [ENTWICKLER]

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
```

## Anwendung

**Für:** Cloud-Migrationen, SaaS-Startups, Enterprise-IT

**Beispiel-Output:** Komplette AWS-Infrastruktur mit ECS Fargate, RDS Aurora, CloudFront, Terraform

**Verkaufspreis:** 8.000-40.000€ je nach Projektgröße

## Variationen

- Für Migration: "On-Premise zu Cloud migrieren"
- Für Multi-Cloud: "Multi-Cloud-Strategie implementieren"
- Für Kosten: "Cloud-Kosten um 50% senken"
- Für Serverless: "Serverless-First Architektur"
