# src/smart_predictor/data/ingest.py

from .api_client import fetch_batch
from .checkpoint import load_checkpoint, save_checkpoint

import pandas as pd
from pathlib import Path

RAW_DATA_DIR = Path("data/raw")


def save_batch(records, offset):
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(records)
    file_path = RAW_DATA_DIR / f"energy_offset_{offset}.parquet"
    df.to_parquet(file_path, index=False)


def ingest_energy_data(base_url, batch_size=10000, max_records=1_000_000):
    checkpoint = load_checkpoint()
    offset = checkpoint["offset"]
    total_fetched = offset

    while total_fetched < max_records:
        params = {
            "limit": batch_size,
            "offset": offset
        }

        response_json = fetch_batch(base_url, params)
        records = response_json.get("results", [])

        if not records:
            break

        save_batch(records, offset)

        offset += len(records)
        total_fetched += len(records)

        save_checkpoint(offset)

    print("Ingestion completed.")
