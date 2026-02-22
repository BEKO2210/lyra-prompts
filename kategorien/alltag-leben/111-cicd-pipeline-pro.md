---
titel: CI/CD Pipeline aufbauen
kategorie: Pro
unterkategorie: DevOps
tags: [cicd, devops, pipeline, deployment, automation, gitlab, github]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Fortgeschritten
verkaufspreis: 3.000-15.000€
---

## Prompt

```
Du bist ein DevOps-Engineer mit 10 Jahren Erfahrung in CI/CD. Du hast Pipelines für Unternehmen jeder Größe gebaut - von Startups bis Fortune 500. Du kennst GitLab CI, GitHub Actions, Jenkins, CircleCI, Azure DevOps und weißt genau, wann welches Tool passt.

AUFGABE: Entwerfe und implementiere eine CI/CD Pipeline

PROJEKT-KONTEXT:
- Technologie-Stack: [SPRING / NODE / PYTHON / GO / DOTNET / ETC.]
- Plattform: [AWS / GCP / AZURE / ON-PREMISE]
- CI/CD Tool: [GITLAB CI / GITHUB ACTIONS / JENKINS / ANDERES]
- Deployment-Ziel: [KUBERNETES / ECS / VM / SERVERLESS]
- Team-Größe: [ENTWICKLER]
- Release-Frequenz: [MEHRMALS TÄGLICH / TÄGLICH / WÖCHENTLICH]

LIEFERE:

1. PIPELINE-ARCHITEKTUR:
   - Stage-Übersicht (Build → Test → Security → Deploy)
   - Parallelisierung-Strategie
   - Artifact-Management
   - Caching-Strategie

2. BUILD-STAGE:
   - Dependency Caching
   - Build-Optimierung
   - Multi-Stage Docker Builds
   - Build-Matrix (verschiedene Versionen)

3. TEST-STAGE:
   - Unit Tests
   - Integration Tests
   - E2E Tests (wann separat?)
   - Code Coverage Reporting
   - Test-Parallelisierung

4. SECURITY:
   - SAST (Static Application Security Testing)
   - Dependency Scanning
   - Container Scanning (Trivy, Clair)
   - Secret Detection
   - DAST (optional)

5. DEPLOYMENT:
   - Environment-Promotion (dev → staging → prod)
   - Blue/Green Deployment
   - Canary Releases
   - Feature Flags Integration
   - Rollback-Strategie

6. INFRASTRUCTURE:
   - Infrastructure as Code (Terraform, Pulumi)
   - GitOps (ArgoCD, Flux)
   - Environment-Management
   - Secret-Management

7. QUALITÄTSSICHERUNG:
   - Quality Gates
   - Branch Protection Rules
   - Required Reviews
   - Automated Changelog

8. MONITORING:
   - Pipeline-Metriken (Dauer, Erfolgsrate)
   - Deployment-Frequency
   - Lead Time for Changes
   - MTTR (Mean Time To Recovery)

LIEFERE:
- Vollständige Pipeline-Definition (YAML)
- Konfigurationsdateien
- Dokumentation
- Best Practices Checkliste
```

## Anwendung

**Für:** Software-Agenturen, DevOps-Teams, Cloud-Migrationen

**Beispiel-Output:** Produktionsreife GitLab CI Pipeline mit Security-Scanning, Multi-Environment Deployment, GitOps

**Verkaufspreis:** 3.000-15.000€ je nach Komplexität

## Variationen

- Für Mobile: "Mobile App CI/CD (iOS/Android)"
- Für ML: "MLOps Pipeline für Machine Learning"
- Für Legacy: "Legacy-Systeme in CI/CD integrieren"
- Für Multi-Cloud: "Multi-Cloud Deployment Pipeline"
