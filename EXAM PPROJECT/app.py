import streamlit as st
import pandas as pd
from src.data import load_and_clean_data
from src.features import engineer_features
from src.models import load_model, predict
import tempfile
import os

st.title('Package Delivery Time Estimation')
st.write('Upload a CSV file with package data (same columns as training, except target).')

# Show evaluation metrics from training
metrics_path = 'outputs/evaluation.txt'
if os.path.exists(metrics_path):
    st.subheader('Model Evaluation Metrics (on training data)')
    with open(metrics_path, 'r') as f:
        metrics_text = f.read()
    st.text(metrics_text)
else:
    st.info('No evaluation metrics found. Run training to generate them.')

uploaded_file = st.file_uploader('Choose a CSV file', type='csv')

if uploaded_file is not None:
    # Save uploaded file to a temp location
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name
    try:
        # Load and preprocess data
        df_new = load_and_clean_data(tmp_path)
        X_new, _ = engineer_features(df_new)
        # Load model
        model = load_model()
        # Predict
        y_pred_new = predict(model, X_new)
        # Show results
        results = df_new.copy()
        results['predicted_delivery_duration'] = y_pred_new
        st.write('### Predictions')
        st.dataframe(results)
        # Download button
        csv = results.to_csv(index=False).encode('utf-8')
        st.download_button('Download predictions as CSV', csv, 'predictions.csv', 'text/csv')
    except Exception as e:
        st.error(f'Error processing file: {e}')
    finally:
        os.remove(tmp_path)
else:
    st.info('Please upload a CSV file to get predictions.') 