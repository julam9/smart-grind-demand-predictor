# src/smart_predictor/data/load.py

from pathlib import Path
import pandas as pd


RAW_DATA_DIR = Path("data/raw")
PROCESSED_DATA_DIR = Path("data/processed")


def load_raw_batches() -> pd.DataFrame:
    """
    Load all raw parquet batch files and concatenate them.
    """
    files = sorted(RAW_DATA_DIR.glob("energy_offset_*.parquet"))

    if not files:
        raise FileNotFoundError("No raw data files found.")

    df_list = [pd.read_parquet(f) for f in files]
    df = pd.concat(df_list, ignore_index=True)

    return df


def load_processed_data(filename: str) -> pd.DataFrame:
    """
    Load processed dataset by filename.
    """
    file_path = PROCESSED_DATA_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(f"{filename} not found in processed data.")

    return pd.read_parquet(file_path)
