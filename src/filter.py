import numpy as np
from scipy.signal import butter, filtfilt, iirnotch

def butter_bandpass(lowcut: float, highcut: float, fs: float, order: int = 4):
    """Generates Butterworth bandpass filter coefficients."""
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def apply_bandpass_filter(data: np.ndarray, lowcut: float = 0.5, highcut: float = 45.0, fs: float = 360.0, order: int = 4) -> np.ndarray:
    """
    Applies a zero-phase Butterworth bandpass filter to remove baseline wander and high-frequency noise.
    
    Parameters:
        data: 1D NumPy array of raw ECG voltage values.
        lowcut: Cutoff for removing baseline wander (default 0.5 Hz).
        highcut: Cutoff for removing high-frequency noise (default 45.0 Hz).
        fs: Sampling frequency in Hz (default 360.0 Hz for MIT-BIH dataset).
        order: Filter order.
    """
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    filtered_data = filtfilt(b, a, data)
    return filtered_data

def apply_notch_filter(data: np.ndarray, powerline_freq: float = 60.0, fs: float = 360.0, quality_factor: float = 30.0) -> np.ndarray:
    """Removes powerline interference (50Hz or 60Hz noise)."""
    nyquist = 0.5 * fs
    freq = powerline_freq / nyquist
    b, a = iirnotch(freq, quality_factor)
    return filtfilt(b, a, data)