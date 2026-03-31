import joblib
import numpy as np

pipeline = joblib.load('stress_pipeline.pkl')

def predict_stress(input_data):
    input_data = np.array(input_data).reshape(1, -1)

    probs = pipeline.predict_proba(input_data)[0]
    pred = np.argmax(probs)

    if pred == 1:
        return "UNDER STRESS", probs[1]
    else:
        return "NO STRESS", probs[0]
