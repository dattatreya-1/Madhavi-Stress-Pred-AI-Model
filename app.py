import streamlit as st
from predict import predict_stress

st.title("Stress Detection App")

# Personality
openness = st.number_input("Openness")
conscientiousness = st.number_input("Conscientiousness")
extraversion = st.number_input("Extraversion")
agreeableness = st.number_input("Agreeableness")
neuroticism = st.number_input("Neuroticism")

# Sleep
sleep_time = st.number_input("Sleep Time")
wake_time = st.number_input("Wake Time")
sleep_duration = st.number_input("Sleep Duration")
psqi_score = st.number_input("PSQI Score")

# Phone usage
call_duration = st.number_input("Call Duration")
num_calls = st.number_input("Number of Calls")
num_sms = st.number_input("Number of SMS")
screen_on_time = st.number_input("Screen On Time")

# Sensors
skin_conductance = st.number_input("Skin Conductance")
accelerometer = st.number_input("Accelerometer")
mobility_radius = st.number_input("Mobility Radius")
mobility_distance = st.number_input("Mobility Distance")

if st.button("Predict"):
    input_data = [
        openness, conscientiousness, extraversion, agreeableness, neuroticism,
        sleep_time, wake_time, sleep_duration, psqi_score,
        call_duration, num_calls, num_sms, screen_on_time,
        skin_conductance, accelerometer, mobility_radius, mobility_distance
    ]

    result, prob = predict_stress(input_data)

    if result == "UNDER STRESS":
        st.error(f"⚠️ UNDER STRESS\nProbability: {prob:.2f}")
    else:
        st.success(f"✅ NO STRESS\nProbability: {prob:.2f}")
