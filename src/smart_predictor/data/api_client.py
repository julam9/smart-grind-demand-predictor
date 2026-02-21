# src/smart_predictor/data/api_client.py

import time
import requests


def fetch_batch(url, params, max_retries=5, timeout=10):
    for attempt in range(max_retries):
        response = requests.get(url, params=params, timeout=timeout)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 429:
            sleep_time = 2 ** attempt
            time.sleep(sleep_time)

        elif 500 <= response.status_code < 600:
            sleep_time = 2 ** attempt
            time.sleep(sleep_time)

        else:
            raise RuntimeError(
                f"Request failed: {response.status_code} - {response.text}"
            )

    raise RuntimeError("Max retries exceeded")
