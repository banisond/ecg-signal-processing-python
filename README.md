![CI / Automated Testing](https://github.com/banisond/ecg-signal-processing-python/actions/workflows/test.yml/badge.svg)

# Biomedical ECG Signal Processing & Peak Detection Starter Kit

A production-grade Python package and FastAPI server for biomedical signal processing, digital noise filtering, R-peak detection, and Heart Rate Variability (HRV) metrics calculation. Designed for digital health startups, wearable integrations, and medical device prototypes.

---

## Key Features

- **Noise Reduction (`src/filter.py`)**: Zero-phase Butterworth bandpass filter (0.5–45 Hz) for baseline wander removal and powerline notch filtering (50/60 Hz).
- **Peak & HRV Analysis (`src/peak_detection.py`)**: QRS complex enhancement, adaptive thresholding for R-peak detection, and automatic extraction of time-domain HRV metrics ($\text{SDNN}$, $\text{RMSSD}$).
- **Production REST API (`app.py`)**: Pre-built FastAPI endpoint (`POST /v1/process-ecg`) for remote array processing with Pydantic validation and interactive Swagger documentation.
- **Containerized & Tested (`tests/`)**: Fully Dockerized deployment with an automated `pytest` suite running in GitHub Actions CI.

---

## Quick Start

### Option 1: Docker (Recommended)
Ensure [Docker Desktop](https://www.docker.com/products/docker-desktop) is running, then launch the containerized API:

```bash
docker compose up --build