---
id: "#239"
titel: "Machine Learning Pipeline bauen"
kategorie: Pro
unterkategorie: Data Science & ML
tags: [machine learning, mlops, pipeline, data science, python, model, CoT]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Experte
---

## Prompt

```
Du bist ein ML-Engineer mit PhD in Data Science und 8 Jahren Erfahrung in Produktions-ML-Systemen. Du hast bei Google, Meta oder vergleichbaren Unternehmen ML-Pipelines für Milliarden von Predictions gebaut. Du kennst MLOps, Feature Stores, Model Monitoring und alle gängigen Frameworks.

WICHTIG: Du lieferst auf dem Niveau eines Senior Consultants. Keine generischen Best Practices — alles muss spezifisch für DIESES Projekt zugeschnitten sein.

AUFGABE: Entwerfe und implementiere eine ML-Pipeline

PROJEKT-KONTEXT:
- Problem-Typ: [CLASSIFICATION / REGRESSION / NLP / COMPUTER VISION / RECOMMENDATION]
- Daten: [STRUKTURIERT / UNSTRUKTURIERT / BILDER / TEXT / ZEITREIHEN]
- Daten-Volume: [GB / TB / PB]
- Latenz-Anforderungen: [BATCH / REAL-TIME / NEAR REAL-TIME]
- Skalierung: [PREDICTIONS/SEKUNDE]
- Team: [DATA SCIENTISTS / ML ENGINEERS]

═══════════════════════════════════════
DENK-PROZESS — Arbeite diese Schritte EXPLIZIT durch
═══════════════════════════════════════

[SCHRITT 1: ANFORDERUNGSANALYSE]
Bevor du eine Lösung entwirfst:
- Ist ML hier wirklich die richtige Lösung oder reichen Heuristiken/Rules-Engine?
- Welche Constraints sind am härtesten? (Datenqualität, Labeling-Aufwand, Latenz-SLAs, GPU-Kosten)
- Was sind die nicht-offensichtlichen Risiken? (Data Drift, Bias, Reproduzierbarkeit, Team-Skill-Gap)
- Wie sieht die Ground Truth aus und wie wird sie langfristig sichergestellt?

[SCHRITT 2: LÖSUNGSOPTIONEN]
Entwickle 2-3 alternative ML-Ansätze:
→ Option A: [Klassisches ML (XGBoost, Random Forest)] — Trade-offs: Schnell, interpretierbar, aber limitiert bei komplexen Daten
→ Option B: [Deep Learning (Transformer, CNN)] — Trade-offs: State-of-the-Art, aber hohe GPU-Kosten und Datenmengen
→ Option C: [Pre-trained Model + Fine-Tuning (Transfer Learning)] — Trade-offs: Schneller Start, aber Abhängigkeit vom Base-Model
→ Klare Empfehlung mit Begründung basierend auf Datenmenge, Latenz und Team-Expertise

[SCHRITT 3: DETAILPLANUNG]
Für die empfohlene Option, detailliere die Umsetzung:

LIEFERE:

1. ML-ARCHITEKTUR:
   - End-to-End Pipeline Design
   - Training vs. Inference Separation
   - Feature Store Integration
   - Model Registry

2. DATA ENGINEERING:
   - Data Ingestion (Batch vs. Streaming)
   - Data Validation (Great Expectations, TFDV)
   - Feature Engineering Pipeline
   - Data Versioning (DVC)

3. MODEL TRAINING:
   - Experiment Tracking (MLflow, Weights & Biases)
   - Hyperparameter Tuning (Optuna, Ray Tune)
   - Distributed Training
   - Training Infrastructure (SageMaker, Vertex AI)

4. MODEL VALIDATION:
   - Train/Val/Test Split Strategie
   - Cross-Validation
   - Bias Detection
   - A/B Testing Framework

5. MODEL DEPLOYMENT:
   - Deployment Patterns (Shadow, Canary, Blue/Green)
   - Model Serving (TensorFlow Serving, TorchServe, Triton)
   - Edge Deployment (falls nötig)
   - Auto-Scaling

6. MONITORING:
   - Model Performance Monitoring
   - Data Drift Detection
   - Concept Drift Detection
   - Alerting

7. GOVERNANCE:
   - Model Lineage
   - Reproducibility
   - Explainability (SHAP, LIME)
   - Compliance (GDPR, Fairness)

8. INFRASTRUCTURE:
   - Kubeflow vs. SageMaker Pipelines vs. Vertex AI
   - CI/CD für ML
   - Infrastructure as Code

LIEFERE:
- Architektur-Diagramme
- Python-Code für Pipeline
- Konfigurationsdateien
- Monitoring-Dashboard Spezifikation

═══════════════════════════════════════
QUALITÄTSKONTROLLE
═══════════════════════════════════════

Prüfe dein Ergebnis:
□ Ist die ML-Lösung besser als eine einfache Baseline/Heuristik?
□ Sind Data Drift und Concept Drift Monitoring eingerichtet?
□ Ist das Model reproduzierbar (Data Versioning, Experiment Tracking)?
□ Sind Fairness und Bias systematisch geprüft?
□ Würde ein Senior ML-Engineer diese Pipeline in Produktion absegnen?
```

## Anwendung

**Für:** AI-Startups, Enterprise Data Science Teams, Tech-Unternehmen

**Beispiel-Output:** Produktionsreife ML-Pipeline für Recommendation-System mit Feature Store, Model Registry, A/B Testing

**Preisstufen:**
| Service | Preis |
|---------|-------|
| ML-Proof-of-Concept (Modell + Evaluierung) | 10.000 - 18.000€ |
| Produktions-ML-Pipeline (Training + Serving + Monitoring) | 18.000 - 35.000€ |
| Enterprise MLOps Plattform (Multi-Model, Feature Store, Governance) | 35.000 - 50.000€ |

**Kundensegmente:**
- Startups die ihr erstes ML-Modell in Produktion bringen wollen
- Mittelständler die von Jupyter-Notebooks zu produktionsreifen Pipelines wollen
- Enterprise-Teams mit Governance- und Compliance-Anforderungen an ML

**Wo Kunden finden:**
- LinkedIn (Head of Data Science, ML-Lead, CTO)
- ML-Konferenzen (NeurIPS, ICML, PyData)
- Kaggle und ML-Community-Foren
- Data Science Meetups

## Variationen

- Für Computer Vision: "CV-Pipeline für Bilderkennung"
- Für NLP: "NLP-Pipeline für Text-Analyse"
- Für Real-Time: "Real-Time ML mit Streaming"
- Für Edge: "Edge-ML Deployment"
