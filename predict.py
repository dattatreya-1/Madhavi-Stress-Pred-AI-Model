import joblib
import numpy as np

pipeline = joblib.load('stress_pipeline.pkl')

def predict_stress(input_data):
    input_data = np.array(input_data).reshape(1, -1)

    probs = pipeline.predict_proba(input_data)[0]

    stress_prob = probs[1]

    # 🔥 Adjust threshold
    if stress_prob > 0.90:
        return "UNDER STRESS", stress_prob
    else:
        return "NO STRESS", probs[0]
