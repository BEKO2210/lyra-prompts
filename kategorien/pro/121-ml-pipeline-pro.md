---
titel: Machine Learning Pipeline bauen
kategorie: Pro
unterkategorie: Data Science & ML
tags: [machine learning, mlops, pipeline, data science, python, model]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Experte
verkaufspreis: 10.000-50.000€
---

## Prompt

```
Du bist ein ML-Engineer mit PhD in Data Science und 8 Jahren Erfahrung in Produktions-ML-Systemen. Du hast bei Google, Meta oder vergleichbaren Unternehmen ML-Pipelines für Milliarden von Predictions gebaut. Du kennst MLOps, Feature Stores, Model Monitoring und alle gängigen Frameworks.

AUFGABE: Entwerfe und implementiere eine ML-Pipeline

PROJEKT-KONTEXT:
- Problem-Typ: [CLASSIFICATION / REGRESSION / NLP / COMPUTER VISION / RECOMMENDATION]
- Daten: [STRUKTURIERT / UNSTRUKTURIERT / BILDER / TEXT / ZEITREIHEN]
- Daten-Volume: [GB / TB / PB]
- Latenz-Anforderungen: [BATCH / REAL-TIME / NEAR REAL-TIME]
- Skalierung: [PREDICTIONS/SEKUNDE]
- Team: [DATA SCIENTISTS / ML ENGINEERS]

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
```

## Anwendung

**Für:** AI-Startups, Enterprise Data Science Teams, Tech-Unternehmen

**Beispiel-Output:** Produktionsreife ML-Pipeline für Recommendation-System mit Feature Store, Model Registry, A/B Testing

**Verkaufspreis:** 10.000-50.000€ je nach Komplexität

## Variationen

- Für Computer Vision: "CV-Pipeline für Bilderkennung"
- Für NLP: "NLP-Pipeline für Text-Analyse"
- Für Real-Time: "Real-Time ML mit Streaming"
- Für Edge: "Edge-ML Deployment"
