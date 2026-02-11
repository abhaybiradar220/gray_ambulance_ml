from fastapi import FastAPI
import numpy as np
import pandas as pd

from src.artifact_handling import handle_artifacts
app = FastAPI(title="Smart Ambulance Risk API")
@app.post("/analyze")
def analyze_vitals(vitals: dict):
    """
    Input: dict with keys:
    heart_rate, spo2, bp_systolic, bp_diastolic, motion
    """

    df = pd.DataFrame([vitals])
    df = handle_artifacts(df)
    #anomaly logic 
    hr_dev = abs(df["heart_rate"].iloc[0] - 75) / 10
    spo2_dev = abs(df["spo2"].iloc[0] - 98) / 2
    anomaly_score = hr_dev + spo2_dev
    anomaly_flag = anomaly_score > 3

    risk_score = min(anomaly_score / 5, 1.0)

    return {
        "anomaly_flag": bool(anomaly_flag),
        "risk_score": float(round(risk_score, 2)),
        "confidence": float(round(1 - min(0.3, df.isna().mean().mean()), 2))
    }

@app.get("/demo")
def demo():
    vitals = {
        "heart_rate": 120,
        "spo2": 92,
        "bp_systolic": 100,
        "bp_diastolic": 65,
        "motion": 0.3
    }

    df = pd.DataFrame([vitals])
    df = handle_artifacts(df)
    
    hr_dev = abs(df["heart_rate"].iloc[0] - 75) / 10
    spo2_dev = abs(df["spo2"].iloc[0] - 98) / 2
    anomaly_score = hr_dev + spo2_dev
    anomaly_flag = anomaly_score > 3
    risk_score = min(anomaly_score / 5, 1.0)
    return {
        "input": vitals,
        "anomaly_flag": bool(anomaly_flag),
        "risk_score": round(risk_score, 2),
        "confidence": round(1 - min(0.3, df.isna().mean().mean()), 2)
    }
@app.get("/")
def root():
    return {
        "message": "Smart Ambulance Risk API is running",
        "endpoints": {
            "docs": "/docs",
            "demo": "/demo",
            "analyze_post": "/analyze"
        }
    }
