import pandas as pd
from sklearn.impute import SimpleImputer

def engineer_features(df):
    """
    Engineers features from the DataFrame:
    - hour and weekday from 'created_at'
    - keeps relevant numeric columns
    Returns X (features) and y (target: delivery_duration)
    """
    X = df.copy()
    # Feature engineering
    X['hour'] = X['created_at'].dt.hour
    X['weekday'] = X['created_at'].dt.weekday
    # Select features (excluding IDs and timestamps)
    feature_cols = [
        'market_id', 'order_protocol', 'total_items', 'subtotal',
        'num_distinct_items', 'min_item_price', 'max_item_price',
        'total_onshift_partners', 'total_busy_partners', 'total_outstanding_orders',
        'hour', 'weekday'
    ]
    X = X[feature_cols]
    y = df['delivery_duration']
    # Impute missing values
    imputer = SimpleImputer(strategy='mean')
    X_imputed = imputer.fit_transform(X)
    X = pd.DataFrame(X_imputed, columns=X.columns, index=X.index)
    y = y.loc[X.index]
    return X, y 