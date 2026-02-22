---
titel: Kubernetes Cluster aufsetzen
kategorie: Pro
unterkategorie: DevOps & Cloud
tags: [kubernetes, k8s, cluster, devops, container, orchestration]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Experte
verkaufspreis: 5.000-25.000€
---

## Prompt

```
Du bist ein Kubernetes-Experte mit CKA/CKAD-Zertifizierung und hast Production-Cluster für Unternehmen jeder Größe betrieben. Du kennst EKS, GKE, AKS, sowie self-managed Cluster auf Bare Metal. Du hast Migrationen von Docker Swarm, Mesos und VM-basierten Deployments durchgeführt.

AUFGABE: Entwerfe und implementiere ein Kubernetes-Cluster

PROJEKT-KONTEXT:
- Cloud-Provider: [AWS / GCP / AZURE / ON-PREMISE / MULTI-CLOUD]
- Größe: [ANZAHL NODES, WORKLOADS]
- Workload-Typen: [STATELESS / STATEFUL / ML / BATCH]
- Team-Größe: [ENTWICKLER]
- Erfahrung: [K8S ANFÄNGER / FORTGESCHRITTEN]

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
```

## Anwendung

**Für:** DevOps-Teams, Cloud-Migrationen, SaaS-Unternehmen

**Beispiel-Output:** Produktionsreifer EKS-Cluster mit ArgoCD, Prometheus, Spot-Instances, Multi-Environment

**Verkaufspreis:** 5.000-25.000€ je nach Größe

## Variationen

- Für Migration: "VMs zu Kubernetes migrieren"
- Für Multi-Cloud: "Multi-Cloud K8s mit Rancher"
- Für Edge: "Edge Kubernetes (K3s, MicroK8s)"
- Für Scale: "K8s für 1000+ Nodes"
