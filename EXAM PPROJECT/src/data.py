import pandas as pd

def load_and_clean_data(filepath):
    """
    Loads the housing dataset, parses timestamps, and cleans the data.
    Adds a 'delivery_duration' column (in minutes).
    Returns a cleaned DataFrame.
    """
    df = pd.read_csv(filepath)
    # Parse timestamps
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['actual_delivery_time'] = pd.to_datetime(df['actual_delivery_time'])
    # Compute delivery duration in minutes
    df['delivery_duration'] = (df['actual_delivery_time'] - df['created_at']).dt.total_seconds() / 60.0
    # Drop rows with missing or negative durations
    df = df.dropna(subset=['delivery_duration'])
    df = df[df['delivery_duration'] > 0]
    return df 