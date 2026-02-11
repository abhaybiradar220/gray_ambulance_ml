import numpy as np

def handle_artifacts(df):
    df = df.copy()

    # Motion-based artifact: SpO2 unreliable during high vibration
    high_motion = df["motion"] > 1.2
    df.loc[high_motion, "spo2"] = np.nan

    # Heart rate spikes (non-physiological)
    hr_jump = df["heart_rate"].diff().abs() > 25
    df.loc[hr_jump, "heart_rate"] = np.nan

    # Interpolate short gaps only (safety)
    df["heart_rate"] = df["heart_rate"].interpolate(limit=5)
    df["spo2"] = df["spo2"].interpolate(limit=5)

    return df
