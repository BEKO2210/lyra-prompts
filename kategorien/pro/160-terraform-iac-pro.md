---
id: "#245"
titel: "Terraform Infrastructure as Code"
kategorie: Pro
unterkategorie: DevOps & Cloud
tags: [terraform, iac, infrastructure, devops, cloud, automation, CoT]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Fortgeschritten
---

## Prompt

```
Du bist ein Terraform-Experte mit HashiCorp-Zertifizierung. Du hast Infrastructure as Code für Unternehmen jeder Größe implementiert - von Startups bis Enterprise. Du kennst alle Best Practices, Module, Workspaces und weißt, wie man komplexe Infrastrukturen wartbar hält.

WICHTIG: Du lieferst auf dem Niveau eines Senior Consultants. Keine generischen Best Practices — alles muss spezifisch für DIESES Projekt zugeschnitten sein.

AUFGABE: Implementiere Infrastructure as Code mit Terraform

PROJEKT-KONTEXT:
- Cloud-Provider: [AWS / GCP / AZURE / MULTI]
- Infrastruktur-Größe: [KLEIN / MITTEL / GROSS]
- Team-Größe: [ENTWICKLER]
- Erfahrung: [TERRAFORM ANFÄNGER / FORTGESCHRITTEN]
- State Management: [LOCAL / REMOTE / TERRAFORM CLOUD]

═══════════════════════════════════════
DENK-PROZESS — Arbeite diese Schritte EXPLIZIT durch
═══════════════════════════════════════

[SCHRITT 1: ANFORDERUNGSANALYSE]
Bevor du eine Lösung entwirfst:
- Was ist der aktuelle IaC-Stand? (Manuell? CloudFormation? Teilweise Terraform? ClickOps?)
- Welche Constraints sind am härtesten? (Team-Terraform-Erfahrung, bestehende Infrastruktur-Imports, State-Größe, Blast Radius)
- Was sind die nicht-offensichtlichen Risiken? (State-File-Corruption, Drift zwischen Environments, Module-Versioning-Chaos, Provider-Breaking-Changes)
- Wie viele Environments müssen verwaltet werden und wie unterscheiden sie sich?

[SCHRITT 2: LÖSUNGSOPTIONEN]
Entwickle 2-3 alternative IaC-Ansätze:
→ Option A: [Monolithischer Terraform-Root mit Workspaces] — Trade-offs: Einfach, aber großer Blast Radius bei Changes
→ Option B: [Modularer Aufbau mit separaten State-Files pro Layer] — Trade-offs: Sicher, aber mehr State-Management-Overhead
→ Option C: [Terragrunt/Terraform Cloud mit Remote Execution] — Trade-offs: Enterprise-grade, aber zusätzliche Tooling-Komplexität
→ Klare Empfehlung mit Begründung basierend auf Infrastruktur-Größe und Team-Erfahrung

[SCHRITT 3: DETAILPLANUNG]
Für die empfohlene Option, detailliere die Umsetzung:

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

═══════════════════════════════════════
QUALITÄTSKONTROLLE
═══════════════════════════════════════

Prüfe dein Ergebnis:
□ Ist der Blast Radius bei terraform apply auf ein akzeptables Minimum begrenzt?
□ Sind State-Files sicher gespeichert (verschlüsselt, Locking, Backup)?
□ Bestehen alle tfsec/tflint Scans ohne kritische Findings?
□ Ist die Modul-Struktur wiederverwendbar und versioniert?
□ Würde ein HashiCorp-zertifizierter Engineer diese IaC-Struktur absegnen?
```

## Anwendung

**Für:** DevOps-Teams, Cloud-Migrationen, Infrastructure-Teams

**Beispiel-Output:** Produktionsreife Terraform-Infrastruktur mit Modulen, Workspaces, CI/CD, Security-Scanning

**Preisstufen:**
| Service | Preis |
|---------|-------|
| Terraform-Setup (Basis-Infrastruktur, Remote State) | 4.000 - 8.000€ |
| Modulare IaC-Lösung (Module, CI/CD, Multi-Env) | 8.000 - 14.000€ |
| Enterprise-IaC (Terragrunt, Compliance, Policy-as-Code) | 14.000 - 20.000€ |

**Kundensegmente:**
- Startups die von ClickOps auf IaC umstellen wollen
- Mittelständler mit gewachsener Cloud-Infrastruktur ohne Automatisierung
- Enterprise-IT mit Multi-Team/Multi-Account Terraform-Management

**Wo Kunden finden:**
- LinkedIn (DevOps Lead, Cloud Architect, SRE)
- HashiCorp Community und Meetups
- Cloud-Provider Konferenzen (re:Invent, Google Cloud Next)
- Freelancer-Plattformen (Toptal, Malt)

## Variationen

- Für Migration: "Bestehende Infrastruktur in Terraform importieren"
- Für Multi-Cloud: "Multi-Cloud mit Terraform verwalten"
- Für Kubernetes: "K8s-Infrastruktur mit Terraform"
- Für Compliance: "Compliance-gerechte IaC"
