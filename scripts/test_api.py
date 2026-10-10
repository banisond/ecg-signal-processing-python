import csv
import json
import urllib.request

API_URL = "http://127.0.0.1:8000/v1/process-ecg"
DATA_PATH = "data/sample_ecg.csv"


def run_test():
    print(f"Reading sample data from {DATA_PATH}...")
    signal_data = []

    with open(DATA_PATH, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                try:
                    signal_data.append(float(row[0]))
                except ValueError:
                    continue

    payload_dict = {
        "raw_signal": signal_data,
        "sampling_rate": 360,
        "powerline_freq": 60,
    }

    print(f"Sending POST request to {API_URL}...")
    payload = json.dumps(payload_dict).encode("utf-8")
    req = urllib.request.Request(
        API_URL, data=payload, headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            print("\nSuccess! API Response:")
            print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"\nError connecting to API: {e}")


if __name__ == "__main__":
    run_test()