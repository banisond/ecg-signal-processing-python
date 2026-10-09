import numpy as np
import pytest
from src.filter import apply_bandpass_filter, apply_notch_filter
from src.peak_detection import detect_r_peaks, calculate_hrv_metrics

def test_bandpass_filter_shape():
    """Verify that output signal length matches input signal length."""
    raw_data = np.random.randn(3600)  # 10 seconds of dummy noise at 360 Hz
    filtered = apply_bandpass_filter(raw_data, fs=360.0)
    assert len(filtered) == len(raw_data)

def test_peak_detection_synthetic():
    """Verify R-peak detection on a clean synthetic peak signal."""
    fs = 360.0
    signal = np.zeros(int(fs * 5))  # 5 seconds = 1800 samples (indices 0 to 1799)
    
    # Space peaks every 300 samples (~0.833 sec apart = 72 BPM)
    peak_indices = [300, 600, 900, 1200, 1500]
    for idx in peak_indices:
        signal[idx] = 2.0  # Spike voltage
        
    detected = detect_r_peaks(signal, fs=fs)
    metrics = calculate_hrv_metrics(detected, fs=fs)
    
    assert len(detected) == len(peak_indices)
    assert metrics["mean_hr_bpm"] == 72.0

def test_empty_peaks_hrv():
    """Verify HRV calculation handles empty peak inputs gracefully."""
    metrics = calculate_hrv_metrics(np.array([]))
    assert metrics["mean_hr_bpm"] == 0.0