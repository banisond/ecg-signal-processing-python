from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import numpy as np

from src.filter import apply_bandpass_filter, apply_notch_filter
from src.peak_detection import detect_r_peaks, calculate_hrv_metrics

app = FastAPI(
    title="MedTech ECG Processing API",
    description="Production pipeline for ECG filtering, R-peak detection, and HRV metrics.",
    version="1.0.0"
)

class ECGRequest(BaseModel):
    raw_signal: List[float]
    sampling_rate: float = 360.0
    powerline_freq: float = 60.0

class ECGResponse(BaseModel):
    filtered_signal: List[float]
    r_peak_indices: List[int]
    metrics: dict

@app.get("/")
def read_root():
    return {"message": "ECG Signal Processing API is online."}

@app.post("/v1/process-ecg", response_model=ECGResponse)
def process_ecg(payload: ECGRequest):
    if not payload.raw_signal:
        raise HTTPException(status_code=400, detail="raw_signal list cannot be empty.")
    
    # Require at least 32 data points so SciPy filter padding works cleanly
    if len(payload.raw_signal) < 32:
        raise HTTPException(
            status_code=400, 
            detail=f"raw_signal must contain at least 32 samples (received {len(payload.raw_signal)})."
        )
    
    signal_array = np.array(payload.raw_signal)
    
    # 1. Apply Bandpass & Notch Filtering
    bandpassed = apply_bandpass_filter(signal_array, fs=payload.sampling_rate)
    filtered = apply_notch_filter(bandpassed, powerline_freq=payload.powerline_freq, fs=payload.sampling_rate)
    
    # 2. Detect R-Peaks
    peaks = detect_r_peaks(filtered, sampling_rate=payload.sampling_rate)
    
    # 3. Extract HRV Metrics
    metrics = calculate_hrv_metrics(peaks, sampling_rate=payload.sampling_rate) 

    return ECGResponse(
        filtered_signal=filtered.tolist(),
        r_peak_indices=peaks,
        metrics=metrics
    )