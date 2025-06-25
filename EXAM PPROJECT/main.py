from src.data import load_and_clean_data
from src.features import engineer_features
from src.models import train_model, predict
from src.metrics import evaluate
import pandas as pd

DATA_PATH = 'data/dataset.csv'
PREDICTIONS_PATH = 'outputs/predictions.csv'

if __name__ == '__main__':
    # Load and clean data
    df = load_and_clean_data(DATA_PATH)
    # Feature engineering
    X, y = engineer_features(df)
    X = X.dropna()
    y = y.loc[X.index]  # Keep y aligned with X
    # Train model
    model = train_model(X, y)
    # Predict
    y_pred = predict(model, X)
    # Save predictions
    pd.DataFrame({'y_true': y, 'y_pred': y_pred}).to_csv(PREDICTIONS_PATH, index=False)
    # Evaluate
    metrics = evaluate(y, y_pred)
    print('Evaluation metrics:', metrics) 