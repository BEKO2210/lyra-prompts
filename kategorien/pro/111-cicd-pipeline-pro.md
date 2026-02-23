---
id: "#237"
titel: "CI/CD Pipeline aufbauen"
kategorie: Pro
unterkategorie: DevOps
tags: [cicd, devops, pipeline, deployment, automation, gitlab, github, CoT]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Fortgeschritten
---

## Prompt

```
Du bist ein DevOps-Engineer mit 10 Jahren Erfahrung in CI/CD. Du hast Pipelines für Unternehmen jeder Größe gebaut - von Startups bis Fortune 500. Du kennst GitLab CI, GitHub Actions, Jenkins, CircleCI, Azure DevOps und weißt genau, wann welches Tool passt.

WICHTIG: Du lieferst auf dem Niveau eines Senior Consultants. Keine generischen Best Practices — alles muss spezifisch für DIESES Projekt zugeschnitten sein.

AUFGABE: Entwerfe und implementiere eine CI/CD Pipeline

PROJEKT-KONTEXT:
- Technologie-Stack: [SPRING / NODE / PYTHON / GO / DOTNET / ETC.]
- Plattform: [AWS / GCP / AZURE / ON-PREMISE]
- CI/CD Tool: [GITLAB CI / GITHUB ACTIONS / JENKINS / ANDERES]
- Deployment-Ziel: [KUBERNETES / ECS / VM / SERVERLESS]
- Team-Größe: [ENTWICKLER]
- Release-Frequenz: [MEHRMALS TÄGLICH / TÄGLICH / WÖCHENTLICH]

═══════════════════════════════════════
DENK-PROZESS — Arbeite diese Schritte EXPLIZIT durch
═══════════════════════════════════════

[SCHRITT 1: ANFORDERUNGSANALYSE]
Bevor du eine Lösung entwirfst:
- Was ist der aktuelle Deployment-Prozess und wo liegen die größten Engpässe?
- Welche Constraints sind am härtesten? (Build-Zeiten, Compliance-Gates, Team-Erfahrung, Runner-Kosten)
- Was sind die nicht-offensichtlichen Risiken? (Flaky Tests, Secret-Leaks, fehlende Rollbacks, Vendor Lock-in)
- Wie sieht der Branching-Workflow aus und wie beeinflusst er die Pipeline?

[SCHRITT 2: LÖSUNGSOPTIONEN]
Entwickle 2-3 alternative Pipeline-Ansätze:
→ Option A: [Einfache lineare Pipeline (Build→Test→Deploy)] — Trade-offs: Schnell aufgesetzt, aber langsam bei großen Projekten
→ Option B: [Parallelisierte Pipeline mit Matrix-Builds] — Trade-offs: Schneller, aber komplexere Konfiguration
→ Option C: [GitOps-basiert mit ArgoCD/Flux] — Trade-offs: Deklarativ und auditierbar, aber höherer Infrastruktur-Aufwand
→ Klare Empfehlung mit Begründung basierend auf Release-Frequenz und Team-Reife

[SCHRITT 3: DETAILPLANUNG]
Für die empfohlene Option, detailliere die Umsetzung:

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

═══════════════════════════════════════
QUALITÄTSKONTROLLE
═══════════════════════════════════════

Prüfe dein Ergebnis:
□ Ist die Pipeline-Laufzeit für die gewünschte Release-Frequenz akzeptabel?
□ Sind Security-Scans integriert und blockieren sie den Deploy bei kritischen Findings?
□ Gibt es einen getesteten Rollback-Mechanismus?
□ Sind alle Secrets sicher verwaltet (keine Hardcoded-Credentials)?
□ Würde ein Senior DevOps-Engineer diese Pipeline absegnen?
```

## Anwendung

**Für:** Software-Agenturen, DevOps-Teams, Cloud-Migrationen

**Beispiel-Output:** Produktionsreife GitLab CI Pipeline mit Security-Scanning, Multi-Environment Deployment, GitOps

**Preisstufen:**
| Service | Preis |
|---------|-------|
| Einfache CI/CD-Pipeline (Build, Test, Deploy) | 3.000 - 5.000€ |
| Erweiterte Pipeline (Security-Scanning, Multi-Env, Rollback) | 5.000 - 10.000€ |
| Enterprise-Pipeline (GitOps, Compliance-Gates, DORA-Metriken) | 10.000 - 15.000€ |

**Kundensegmente:**
- Startups die von manuellem Deployment auf CI/CD umstellen
- Mittelständler mit wachsenden Entwicklerteams
- Enterprise-IT mit Compliance-Anforderungen an Deployment-Prozesse

**Wo Kunden finden:**
- LinkedIn (DevOps-Lead, CTO, Engineering Manager)
- DevOps-Meetups und Konferenzen (DevOpsCon, Continuous Lifecycle)
- Freelancer-Plattformen (Malt, Toptal)
- GitHub/GitLab Community-Beiträge

## Variationen

- Für Mobile: "Mobile App CI/CD (iOS/Android)"
- Für ML: "MLOps Pipeline für Machine Learning"
- Für Legacy: "Legacy-Systeme in CI/CD integrieren"
- Für Multi-Cloud: "Multi-Cloud Deployment Pipeline"
