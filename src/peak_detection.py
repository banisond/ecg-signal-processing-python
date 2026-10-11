import numpy as np
from scipy.signal import find_peaks

def detect_r_peaks(filtered_signal: list[float], sampling_rate: int = 360) -> list[int]:
    """
    Detect R-peaks in an ECG signal using dynamic thresholding.
    Returns a clean list of Python integers for JSON serialization.
    """
    signal = np.array(filtered_signal, dtype=float)
    if len(signal) == 0:
        return []

    min_distance = int(sampling_rate * 0.35)
    signal_mean = float(np.mean(signal))
    signal_std = float(np.std(signal))
    dynamic_height = signal_mean + (0.5 * signal_std)
    dynamic_prominence = (0.3 * signal_std) if signal_std > 0 else None

    peaks, _ = find_peaks(
        signal,
        distance=max(1, min_distance),
        height=dynamic_height,
        prominence=dynamic_prominence
    )

    if isinstance(peaks, np.ndarray):
        return peaks.tolist()
    return [int(p) for p in peaks]

def calculate_hrv_metrics(r_peaks: list[int], sampling_rate: int = 360) -> dict:
    """
    Calculate mean heart rate (BPM) and time-domain HRV metrics (SDNN, RMSSD).
    """
    if len(r_peaks) < 2:
        return {
            "mean_hr_bpm": 0.0,
            "sdnn_ms": 0.0,
            "rmssd_ms": 0.0
        }

    # Calculate RR intervals in milliseconds
    rr_intervals_ms = (np.diff(r_peaks) / float(sampling_rate)) * 1000.0

    mean_rr = float(np.mean(rr_intervals_ms))
    mean_hr = 60000.0 / mean_rr if mean_rr > 0 else 0.0
    sdnn = float(np.std(rr_intervals_ms, ddof=1)) if len(rr_intervals_ms) > 1 else 0.0
    
    successive_diffs = np.diff(rr_intervals_ms)
    rmssd = float(np.sqrt(np.mean(successive_diffs ** 2))) if len(successive_diffs) > 0 else 0.0

    return {
        "mean_hr_bpm": round(mean_hr, 1),
        "sdnn_ms": round(sdnn, 1),
        "rmssd_ms": round(rmssd, 1)
    }