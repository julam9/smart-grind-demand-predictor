# columns names still need to be adjusted
import pandas as pd

def preprocess_raw_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and standardize raw energy consumption data.

    Expected columns (example):
        - timestamp
        - demand

    Returns:
        Cleaned DataFrame sorted by timestamp.
    """

    df = df.copy()

    # -----------------------------
    # 1. Standardize column names
    # -----------------------------
    df.columns = df.columns.str.lower().str.strip()

    # -----------------------------
    # 2. Ensure timestamp column exists
    # -----------------------------
    if "timestamp" not in df.columns:
        raise ValueError("Expected 'timestamp' column not found.")

    # -----------------------------
    # 3. Convert timestamp to datetime
    # -----------------------------
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Remove invalid timestamps
    df = df.dropna(subset=["timestamp"])

    # -----------------------------
    # 4. Sort chronologically
    # -----------------------------
    df = df.sort_values("timestamp")

    # -----------------------------
    # 5. Remove duplicate timestamps
    # -----------------------------
    df = df.drop_duplicates(subset=["timestamp"])

    # -----------------------------
    # 6. Ensure demand column exists
    # -----------------------------
    if "demand" not in df.columns:
        raise ValueError("Expected 'demand' column not found.")

    # -----------------------------
    # 7. Handle missing demand values
    # -----------------------------
    df["demand"] = pd.to_numeric(df["demand"], errors="coerce")

    # Option 1: Drop missing
    df = df.dropna(subset=["demand"])

    # Option 2 (alternative): Forward fill
    # df["demand"] = df["demand"].fillna(method="ffill")

    # -----------------------------
    # 8. Reset index
    # -----------------------------
    df = df.reset_index(drop=True)

    return df