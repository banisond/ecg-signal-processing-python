import numpy as np
from scipy.signal import find_peaks

def detect_r_peaks(filtered_ecg: np.ndarray, fs: float = 360.0, min_distance_ms: float = 200.0) -> np.ndarray:
    """
    Detects R-peaks in a filtered ECG signal using adaptive thresholding.
    
    Parameters:
        filtered_ecg: 1D NumPy array of filtered ECG voltage values.
        fs: Sampling rate in Hz.
        min_distance_ms: Minimum refractory period between consecutive R-peaks in milliseconds.
        
    Returns:
        1D NumPy array of sample indices corresponding to detected R-peaks.
    """
    min_distance_samples = int((min_distance_ms / 1000.0) * fs)
    
    # Square signal to highlight high-frequency QRS complexes
    squared_signal = np.square(filtered_ecg)
    
    # Set peak height threshold relative to signal power
    threshold = np.mean(squared_signal) + 1.5 * np.std(squared_signal)
    
    peaks, _ = find_peaks(squared_signal, distance=min_distance_samples, height=threshold)
    return peaks

def calculate_hrv_metrics(r_peaks: np.ndarray, fs: float = 360.0) -> dict:
    """
    Calculates Heart Rate (BPM) and basic HRV metrics (SDNN, RMSSD).
    """
    if len(r_peaks) < 2:
        return {"mean_hr_bpm": 0.0, "sdnn_ms": 0.0, "rmssd_ms": 0.0}
    
    # Calculate RR intervals in milliseconds
    rr_intervals_ms = (np.diff(r_peaks) / fs) * 1000.0
    
    mean_hr_bpm = 60000.0 / np.mean(rr_intervals_ms)
    sdnn_ms = np.std(rr_intervals_ms)
    rmssd_ms = np.sqrt(np.mean(np.square(np.diff(rr_intervals_ms))))
    
    return {
        "mean_hr_bpm": round(float(mean_hr_bpm), 2),
        "sdnn_ms": round(float(sdnn_ms), 2),
        "rmssd_ms": round(float(rmssd_ms), 2)
    }