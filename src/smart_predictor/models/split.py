import pandas as pd

def time_series_split(df: pd.DataFrame, train_ratio=0.7, val_ratio=0.15):
    """
    Chronological split.
    """

    n = len(df)
    train_end = int(n * train_ratio)
    val_end = int(n * (train_ratio + val_ratio))

    train = df.iloc[:train_end]
    val = df.iloc[train_end:val_end]
    test = df.iloc[val_end:]

    return train, val, test