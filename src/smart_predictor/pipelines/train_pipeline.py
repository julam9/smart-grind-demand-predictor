from smart_predictor.data.load import load_raw_batches
from smart_predictor.data.preprocess import preprocess_raw_data
from smart_predictor.features.build_features import (
    aggregate_daily,
    create_lag_features,
)
from smart_predictor.models.split import time_series_split 
from smart_predictor.model.train import train_linear_regression, evaluate_model

def run_training_pipeline():
    # Load raw data
    df_raw = load_raw_batches()

    # Clean
    df_clean = preprocess_raw_data(df_raw)

    # Aggregate to daily
    df_daily = aggregate_daily(df_clean)

    # Feature engineering
    df_features = create_lag_features(df_daily)

    # Shift the target variable to predict the next day's demand
    df_features['target'] = df_features['daily_demand'].shift(-1)
    df_features = df_features.dropna().reset_index(drop=True)
    
    # Split
    train, val, test = time_series_split(df_features)

    # Separate features and target 
    feature_cols = [ 
                    "lag_1",
                    "lag_7",
                    "lag_14",
                    "rolling_7", 
                    "rolling_30",
                    "day_of_week", 
                    "month",
                    ]
    
    X_train = train[feature_cols]
    y_train = train["target"]
    
    X_val = val[feature_cols]
    y_val = val["target"]

    X_test = test[feature_cols] 
    y_test = test["target"]    
    
    # Train the model 
    model = train_linear_regression(X_train, y_train) 
    
    # Evaluate 
    train_metrics = evaluate_model(model, X_train, y_train)
    val_metrics = evaluate_model(model, X_val, y_val)
    test_metrics = evaluate_model(model, X_test, y_test)
    
    print(f"Train evaluation:", train_metrics)
    print(f"Validation evaluation:", val_metrics)
    print(f"Test evaluation:", test_metrics)

if __name__ == "__main__":
    run_training_pipeline()