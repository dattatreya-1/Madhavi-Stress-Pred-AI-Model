import streamlit as st
from predict import predict_stress

st.title("Stress Detection App")

st.write("Enter the details below:")

# Example inputs (adjust based on your dataset)
sleep_duration = st.number_input("Sleep Duration")
call_duration = st.number_input("Call Duration")
num_calls = st.number_input("Number of Calls")
num_sms = st.number_input("Number of SMS")
screen_on_time = st.number_input("Screen On Time")
mobility_distance = st.number_input("Mobility Distance")

if st.button("Predict"):
    input_data = [
        sleep_duration,
        call_duration,
        num_calls,
        num_sms,
        screen_on_time,
        mobility_distance
    ]

    result, prob = predict_stress(input_data)

    if result == "UNDER STRESS":
        st.error(f"⚠️ Person is UNDER STRESS\n\nProbability = {prob:.2f}")
    else:
        st.success(f"✅ Person is NOT STRESSED\n\nProbability = {prob:.2f}")
