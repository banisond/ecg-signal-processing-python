import os
import matplotlib.pyplot as plt
import numpy as np
from src.filter import apply_bandpass_filter, apply_notch_filter
from src.peak_detection import detect_r_peaks

# Ensure the assets directory exists
os.makedirs("assets", exist_ok=True)

# Generate a synthetic ECG-like signal for demonstration
fs = 360.0
t = np.linspace(0, 5, int(5 * fs))  # 5 seconds
raw = np.sin(2 * np.pi * 1.2 * t) + np.random.normal(0, 0.2, len(t))

# Process the signal using your package functions
filtered = apply_bandpass_filter(raw, lowcut=0.5, highcut=45.0, fs=fs)
filtered = apply_notch_filter(filtered, powerline_freq=60.0, fs=fs)

# Detect peaks (passing list and correct keyword argument)
peak_indices = detect_r_peaks(filtered.tolist(), sampling_rate=int(fs))
peaks = np.array(peak_indices)

# Create the comparison plot
plt.figure(figsize=(10, 4))
plt.plot(t, raw, label="Raw ECG (With Noise)", alpha=0.5, color="gray")
plt.plot(t, filtered, label="Filtered ECG (Butterworth + Notch)", color="#2b6cb0", linewidth=1.5)
plt.plot(t[peaks], filtered[peaks], "ro", label="Detected R-Peaks", markersize=6)

plt.title("Biomedical ECG Starter Kit: Signal Processing Pipeline")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude (mV)")
plt.legend(loc="upper right")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

# Save the plot
output_path = "assets/ecg_plot.png"
plt.savefig(output_path, dpi=300)
