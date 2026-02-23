from smart_predictor.data.load import load_raw_batches
from smart_predictor.data.preprocess import preprocess_raw_data
from smart_predictor.features.build_features import (
    aggregate_daily,
    create_lag_features,
)
from smart_predictor.models.split import time_series_split

def run_training_pipeline():
    # Load raw data
    df_raw = load_raw_batches()

    # Clean
    df_clean = preprocess_raw_data(df_raw)

    # Aggregate to daily
    df_daily = aggregate_daily(df_clean)

    # Feature engineering
    df_features = create_lag_features(df_daily)

    # Split
    train, val, test = time_series_split(df_features)

    print(f"Train size: {len(train)}")
    print(f"Validation size: {len(val)}")
    print(f"Test size: {len(test)}")


if __name__ == "__main__":
    run_training_pipeline()