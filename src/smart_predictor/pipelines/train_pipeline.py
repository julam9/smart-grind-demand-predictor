from smart_predictor.data.load import load_raw_batches
from smart_predictor.data.preprocess import preprocess_raw_data


def run_training_pipeline():
    df_raw = load_raw_batches()
    df_clean = preprocess_raw_data(df_raw)

    print("Pipeline executed successfully.")


if __name__ == "__main__":
    run_training_pipeline()