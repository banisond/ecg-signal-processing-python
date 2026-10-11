# tests/test_api.py
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "ECG Signal Processing API is online."}

def test_process_ecg_empty_signal():
    response = client.post("/v1/process-ecg", json={"raw_signal": []})
    assert response.status_code == 400
    assert "cannot be empty" in response.json()["detail"]

def test_process_ecg_too_short():
    response = client.post("/v1/process-ecg", json={"raw_signal": [1.0, 2.0, 3.0]})
    assert response.status_code == 400
    assert "at least 32 samples" in response.json()["detail"]

def test_process_ecg_valid_synthetic_signal():
    # Generate a dummy valid signal of 100 zeros/small values (must be >= 32 samples)
    dummy_signal = [0.1 * (i % 10) for i in range(360)]
    
    response = client.post("/v1/process-ecg", json={
        "raw_signal": dummy_signal,
        "sampling_rate": 360.0,
        "powerline_freq": 60.0
    })
    
    assert response.status_code == 200
    data = response.json()
    
    # Check response structure
    assert "filtered_signal" in data
    assert "r_peak_indices" in data
    assert "metrics" in data
    
    # Check that metrics keys exist
    metrics = data["metrics"]
    assert "mean_hr_bpm" in metrics
    assert "sdnn_ms" in metrics
    assert "rmssd_ms" in metrics