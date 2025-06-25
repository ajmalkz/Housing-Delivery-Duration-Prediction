from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def evaluate(y_true, y_pred, output_path='outputs/evaluation.txt'):
    """
    Evaluates predictions and saves MAE, MSE, RMSE to a text file.
    Returns a dictionary of metrics.
    """
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    metrics = {
        'MAE': mae,
        'MSE': mse,
        'RMSE': rmse
    }
    with open(output_path, 'w') as f:
        for k, v in metrics.items():
            f.write(f'{k}: {v:.4f}\n')
    return metrics 