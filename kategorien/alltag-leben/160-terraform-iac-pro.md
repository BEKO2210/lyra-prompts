---
titel: Terraform Infrastructure as Code
kategorie: Pro
unterkategorie: DevOps & Cloud
tags: [terraform, iac, infrastructure, devops, cloud, automation]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Fortgeschritten
verkaufspreis: 4.000-20.000€
---

## Prompt

```
Du bist ein Terraform-Experte mit HashiCorp-Zertifizierung. Du hast Infrastructure as Code für Unternehmen jeder Größe implementiert - von Startups bis Enterprise. Du kennst alle Best Practices, Module, Workspaces und weißt, wie man komplexe Infrastrukturen wartbar hält.

AUFGABE: Implementiere Infrastructure as Code mit Terraform

PROJEKT-KONTEXT:
- Cloud-Provider: [AWS / GCP / AZURE / MULTI]
- Infrastruktur-Größe: [KLEIN / MITTEL / GROSS]
- Team-Größe: [ENTWICKLER]
- Erfahrung: [TERRAFORM ANFÄNGER / FORTGESCHRITTEN]
- State Management: [LOCAL / REMOTE / TERRAFORM CLOUD]

LIEFERE:

1. PROJEKT-SETUP:
   - Verzeichnisstruktur (Best Practices)
   - Terraform Version Management (tfenv)
   - Provider-Konfiguration
   - Backend-Konfiguration (S3, GCS, etc.)
   - State Locking (DynamoDB, etc.)

2. MODULARISIERUNG:
   - Modul-Struktur
   - Wiederverwendbare Module
   - Modul-Versioning
   - Modul-Registry (privat)
   - Komposition Patterns

3. VARIABLEN UND KONFIGURATION:
   - tfvars-Dateien (per Environment)
   - Sensitive Data (Vault, SSM)
   - Validations
   - Locals für Berechnungen

4. WORKSPACES:
   - Workspace-basierte Environments
   - Alternativen (Directory-basiert)
   - Workspace-Auswahl
   - Environment-spezifische Konfig

5. STATE MANAGEMENT:
   - Remote State
   - State Locking
   - State Import
   - State Manipulation (mv, rm)
   - State Backup

6. CI/CD INTEGRATION:
   - Terraform in Pipeline (GitHub Actions, GitLab CI)
   - terraform plan auf PR
   - terraform apply auf Merge
   - Approval Gates
   - Terraform Cloud/Enterprise

7. TESTING:
   - terraform validate
   - terraform fmt
   - tflint
   - tfsec (Security Scanning)
   - Terratest (Integration Tests)

8. DOKUMENTATION:
   - README für Module
   - terraform-docs
   - Architecture Decision Records
   - Runbooks

LIEFERE:
- Terraform-Code (HCL)
- Verzeichnisstruktur
- CI/CD-Pipeline
- Dokumentation
```

## Anwendung

**Für:** DevOps-Teams, Cloud-Migrationen, Infrastructure-Teams

**Beispiel-Output:** Produktionsreife Terraform-Infrastruktur mit Modulen, Workspaces, CI/CD, Security-Scanning

**Verkaufspreis:** 4.000-20.000€ je nach Infrastruktur-Größe

## Variationen

- Für Migration: "Bestehende Infrastruktur in Terraform importieren"
- Für Multi-Cloud: "Multi-Cloud mit Terraform verwalten"
- Für Kubernetes: "K8s-Infrastruktur mit Terraform"
- Für Compliance: "Compliance-gerechte IaC"
