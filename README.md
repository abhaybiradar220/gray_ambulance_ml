#  Early Warning and Risk Scoring System for Smart Ambulance Monitoring
**AI/ML Engineer Internship Assignment | Gray Mobility**

This repository contains the implementation of a safety-aware early warning system designed for ambulance-based physiological monitoring. The system focuses on distinguishing true clinical deterioration from motion-induced artifacts in high-vibration environments.

---

##  Problem Context
Unlike stable ICU environments, physiological data streamed from an ambulance is significantly impacted by vehicle motion and sensor instability. These environmental factors often lead to "alarm fatigue," where frequent false positives caused by mechanical vibration diminish the utility of the monitoring system. 

This implementation provides a modular pipeline to filter motion artifacts and provide adaptive, patient-specific risk scoring.

---

##  System Architecture
The project is organized into a modular pipeline to ensure engineering discipline and reproducibility:

1. **Data Generation:** 30-minute high-fidelity synthetic data (1Hz) simulating baseline transport, clinical distress scenarios, and sensor artifacts.
2. **Artifact Handling:** Explicit signal processing layer to filter motion-induced SpO2 drops and HR spikes using vibration sensor correlation.
3. **Adaptive Monitoring:** A rolling baseline approach designed to detect early warning signals rather than relying on static medical thresholds.
4. **Risk Scoring:** Multi-vital triage logic that combines physiological trends into a priority score with confidence estimates.

---

## 📊 Performance & Evaluation
Evaluation is based on clinical trade-offs between detection sensitivity and alert reliability:

| Metric | Value | Technical Context |
| :--- | :--- | :--- |
| **Alert Latency** | **~1 Second** | Minimal delay suitable for real-time response. |
| **Precision** | **0.254** | Reflects trade-off between motion artifact suppression and sensitivity. |
| **Recall** | **0.257** | Captures deterioration events within noisy time-series data. |
| **Accuracy** | **0.812** | Overall classification performance of the anomaly detection model. |

---

##  Safety-Critical Design
The system is designed as a **Decision Support Tool**, prioritizing human-in-the-loop oversight. 

**Key Design Principles:**
* **Treatment Authority:** The final treatment decision remains with the paramedic; the AI acts as a verification layer.
* **Triage Logic:** Human intuition is required for multi-patient scenes and ethical trade-offs.
* **Safety Gate:** Paramedics retain the ability to override alerts based on visual clinical assessment.

---

##  Deployment & Engineering
The solution is exposed as a production-ready **FastAPI** service.

### Setup Instructions
1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/abhaybiradar220/gray_ambulance_ml.git](https://github.com/abhaybiradar220/gray_ambulance_ml.git)
   cd gray_ambulance_ml
