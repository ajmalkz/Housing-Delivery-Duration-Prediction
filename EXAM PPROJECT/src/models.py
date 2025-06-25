import joblib
from sklearn.linear_model import LinearRegression

MODEL_PATH = 'models/linear_regression.pkl'

def train_model(X, y):
    """
    Trains a linear regression model and saves it to disk.
    Returns the trained model.
    """
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    return model

def load_model():
    """
    Loads the trained model from disk.
    """
    return joblib.load(MODEL_PATH)

def predict(model, X):
    """
    Makes predictions using the trained model.
    """
    return model.predict(X) 