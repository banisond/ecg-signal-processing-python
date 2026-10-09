![CI / Automated Testing](https://github.com/banisond/ecg-signal-processing-python/actions/workflows/test.yml/badge.svg)

# Biomedical ECG Signal Processing & Peak Detection Starter Kit

Production-grade Python pipeline for ECG baseline wander removal, noise filtering, and R-peak / HRV extraction.

A production-grade Python package and API wrapper for biomedical signal processing, digital noise filtering, R-peak detection, and Heart Rate Variability (HRV) metrics calculation. Designed for digital health startups, wearable integration, and medical device software.

## Features

- **Noise Reduction (`src/filter.py`)**: Zero-phase Butterworth bandpass filter (0.5 Hz - 45 Hz) for baseline wander removal and powerline notch filtering (60 Hz).
- **Peak & HRV Analysis (`src/peak_detection.py`)**: QRS complex enhancement, adaptive thresholding for R-peak detection, and automatic extraction of time-domain HRV metrics (SDNN, RMSSD).
- **REST API Ready (`app.py`)**: Pre-built FastAPI endpoints for real-time remote signal array processing with full input validation.
- **Automated Validation (`tests/`)**: Pre-configured `pytest` suite ensuring robust array boundary and edge-case handling.

---

## Quick Start

### 1. Installation

```bash
git clone [https://github.com/banisond/ecg-signal-processing-python.git](https://github.com/banisond/ecg-signal-processing-python.git)
cd ecg-signal-processing-python

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt