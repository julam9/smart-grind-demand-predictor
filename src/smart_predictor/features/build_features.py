import pandas as pd

def aggregate_daily(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate raw timestamped data into daily total demand.
    Assumes df contains:
        - timestamp
        - demand
    """

    df = df.copy()

    df["date"] = df["timestamp"].dt.date

    daily = (
        df.groupby("date", as_index=False)["demand"]
        .sum()
        .rename(columns={"demand": "daily_demand"})
    )

    daily["date"] = pd.to_datetime(daily["date"])
    daily = daily.sort_values("date").reset_index(drop=True)

    return daily


def create_lag_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create deterministic lag and rolling features.
    Must be sorted by date.
    """

    df = df.copy()
    df = df.sort_values("date")

    # Lags (safe: strictly past)
    df["lag_1"] = df["daily_demand"].shift(1)
    df["lag_7"] = df["daily_demand"].shift(7)
    df["lag_14"] = df["daily_demand"].shift(14)

    # Rolling means (shift first to avoid leakage)
    df["rolling_7"] = df["daily_demand"].shift(1).rolling(7).mean()
    df["rolling_30"] = df["daily_demand"].shift(1).rolling(30).mean()

    # Calendar features (safe)
    df["day_of_week"] = df["date"].dt.dayofweek
    df["month"] = df["date"].dt.month

    df = df.dropna().reset_index(drop=True)

    return df