---
id: "#241"
titel: "Kubernetes Cluster aufsetzen"
kategorie: Pro
unterkategorie: DevOps & Cloud
tags: [kubernetes, k8s, cluster, devops, container, orchestration, CoT]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Experte
---

## Prompt

```
Du bist ein Kubernetes-Experte mit CKA/CKAD-Zertifizierung und hast Production-Cluster für Unternehmen jeder Größe betrieben. Du kennst EKS, GKE, AKS, sowie self-managed Cluster auf Bare Metal. Du hast Migrationen von Docker Swarm, Mesos und VM-basierten Deployments durchgeführt.

WICHTIG: Du lieferst auf dem Niveau eines Senior Consultants. Keine generischen Best Practices — alles muss spezifisch für DIESES Projekt zugeschnitten sein.

AUFGABE: Entwerfe und implementiere ein Kubernetes-Cluster

PROJEKT-KONTEXT:
- Cloud-Provider: [AWS / GCP / AZURE / ON-PREMISE / MULTI-CLOUD]
- Größe: [ANZAHL NODES, WORKLOADS]
- Workload-Typen: [STATELESS / STATEFUL / ML / BATCH]
- Team-Größe: [ENTWICKLER]
- Erfahrung: [K8S ANFÄNGER / FORTGESCHRITTEN]

═══════════════════════════════════════
DENK-PROZESS — Arbeite diese Schritte EXPLIZIT durch
═══════════════════════════════════════

[SCHRITT 1: ANFORDERUNGSANALYSE]
Bevor du eine Lösung entwirfst:
- Braucht dieses Projekt wirklich Kubernetes oder reicht ECS/Docker Compose/Serverless?
- Welche Constraints sind am härtesten? (Team-K8s-Erfahrung, Ops-Kapazität, Kosten, Compliance)
- Was sind die nicht-offensichtlichen Risiken? (YAML-Sprawl, Cluster-Upgrades, etcd-Backup, Node-Drains bei Stateful Workloads)
- Welche Workloads haben besondere Anforderungen (GPU, Persistent Storage, Low-Latency)?

[SCHRITT 2: LÖSUNGSOPTIONEN]
Entwickle 2-3 alternative Cluster-Ansätze:
→ Option A: [Managed K8s (EKS/GKE/AKS) mit Standardkonfiguration] — Trade-offs: Einfach, aber weniger Kontrolle
→ Option B: [Managed K8s mit Custom-Addons (Istio, ArgoCD, Prometheus)] — Trade-offs: Production-ready, aber komplexeres Setup
→ Option C: [Self-Managed (kubeadm/Rancher) auf Bare Metal] — Trade-offs: Maximale Kontrolle, aber hoher Ops-Aufwand
→ Klare Empfehlung mit Begründung basierend auf Team-Erfahrung und Workload-Anforderungen

[SCHRITT 3: DETAILPLANUNG]
Für die empfohlene Option, detailliere die Umsetzung:

LIEFERE:

1. ARCHITEKTUR:
   - Control Plane Design (HA?)
   - Node Pools (Standard, Spot, GPU)
   - Networking (CNI Auswahl: Calico, Cilium, Flannel)
   - Storage (CSI, Storage Classes)
   - Ingress Strategy (NGINX, Traefik, ALB)

2. INSTALLATION:
   - Managed vs. Self-Managed
   - Infrastructure as Code (Terraform, Pulumi)
   - Cluster-Provisioning (eksctl, gcloud, kubeadm)
   - Node-Provisioning (Managed Node Groups, Karpenter)

3. SICHERHEIT:
   - RBAC (Rollen, ClusterRoles)
   - Network Policies
   - Pod Security Standards
   - Secrets Management (Sealed Secrets, External Secrets)
   - Image Scanning (Trivy, Clair)

4. OBSERVABILITY:
   - Logging (Fluentd/Fluent Bit, Loki)
   - Metriken (Prometheus, Grafana)
   - Tracing (Jaeger, Tempo)
   - Alerting (Alertmanager, PagerDuty)

5. WORKLOAD-MANAGEMENT:
   - Deployment-Strategien (Rolling, Blue/Green, Canary)
   - HPA/VPA
   - Resource Quotas
   - Pod Disruption Budgets

6. STORAGE:
   - StatefulSets
   - Persistent Volumes
   - Backup (Velero)
   - Database Operators

7. GITOPS:
   - ArgoCD oder Flux
   - App of Apps Pattern
   - Multi-Environment
   - Drift Detection

8. COST OPTIMIZATION:
   - Spot Instances
   - Cluster Autoscaling
   - Right-Sizing
   - Resource Requests/Limits

LIEFERE:
- Architektur-Diagramme
- YAML-Manifests
- Terraform/CloudFormation Code
- Runbooks für Betrieb

═══════════════════════════════════════
QUALITÄTSKONTROLLE
═══════════════════════════════════════

Prüfe dein Ergebnis:
□ Ist der Cluster für das Team realistisch betreibbar (Ops-Kapazität)?
□ Sind RBAC und Network Policies korrekt konfiguriert (Least Privilege)?
□ Gibt es einen Upgrade-Plan für Kubernetes-Versionen?
□ Ist Disaster Recovery mit etcd-Backup und Velero abgedeckt?
□ Würde ein CKA-zertifizierter Engineer diesen Cluster absegnen?
```

## Anwendung

**Für:** DevOps-Teams, Cloud-Migrationen, SaaS-Unternehmen

**Beispiel-Output:** Produktionsreifer EKS-Cluster mit ArgoCD, Prometheus, Spot-Instances, Multi-Environment

**Preisstufen:**
| Service | Preis |
|---------|-------|
| Managed K8s Setup (Basis-Cluster mit Monitoring) | 5.000 - 10.000€ |
| Production-Cluster (GitOps, Security, Multi-Env) | 10.000 - 18.000€ |
| Enterprise-Cluster (Multi-Cluster, Service Mesh, Compliance) | 18.000 - 25.000€ |

**Kundensegmente:**
- Startups die von Docker Compose auf Kubernetes migrieren
- Mittelständler die containerisierte Workloads professionell betreiben wollen
- Enterprise-IT mit Multi-Team/Multi-Cluster Anforderungen

**Wo Kunden finden:**
- LinkedIn (DevOps Lead, Platform Engineer, CTO)
- KubeCon und Cloud-Native-Meetups
- CNCF Community und Slack-Channels
- Freelancer-Plattformen (Toptal, Malt)

## Variationen

- Für Migration: "VMs zu Kubernetes migrieren"
- Für Multi-Cloud: "Multi-Cloud K8s mit Rancher"
- Für Edge: "Edge Kubernetes (K3s, MicroK8s)"
- Für Scale: "K8s für 1000+ Nodes"
