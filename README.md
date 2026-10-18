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
```


### Option 2: Local Development
1. Clone the repository and set up a virtual environment:
    ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   
2. Install dependencies:```bash
    ```bash
    pip install -r requirements.txt
    ```
    
3. Run the FastAPI server:
    ```bash
    uvicorn app:app --reload
    ```

---

## 📡 API Usage Example

You can send a raw ECG signal array to the processing endpoint using `curl`:

```bash
curl -X 'POST' \
  'http://localhost:8000/v1/process-ecg' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "raw_signal": [0.0, 0.2, 0.5, 1.2, 3.5, 1.1, 0.3, 0.1, 0.0, -0.1],
  "sampling_rate": 250.0,
  "powerline_freq": 60.0
}'

```

---

## 🧪 Running Tests

To run the automated test suite locally with `pytest`:

```bash
pytest

```

---

## 🤝 Contributing

Contributions are welcome! Please check out our [CONTRIBUTING.md](https://www.google.com/search?q=CONTRIBUTING.md) guide for details on setting up your environment, running tests, and submitting pull requests.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

```

```