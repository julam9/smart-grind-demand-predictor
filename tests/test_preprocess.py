import pandas as pd
from smart_predictor.data.preprocess import preprocess_raw_data


def test_preprocess_removes_duplicates():
    df = pd.DataFrame({
        "timestamp": ["2024-01-01", "2024-01-01"],
        "demand": [100, 100]
    })

    result = preprocess_raw_data(df)

    assert len(result) == 1


def test_preprocess_converts_timestamp():
    df = pd.DataFrame({
        "timestamp": ["2024-01-01"],
        "demand": [100]
    })

    result = preprocess_raw_data(df)

    assert pd.api.types.is_datetime64_any_dtype(result["timestamp"])