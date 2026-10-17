import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the saved model
model = joblib.load('best_svc_model.joblib')

# Set page configuration
st.set_page_config(
    page_title="Delivery Delay Predictor",
    page_icon="🚚",
    layout="centered"
)

st.title("🚚 Delivery Delay Prediction App")
st.write("Enter the delivery details below to predict whether a delivery will be delayed or on-time.")

# Create two columns for input fields
col1, col2 = st.columns(2)

with col1:
    delivery_distance = st.number_input("Delivery Distance (miles)", min_value=0.0, value=20.0, step=1.0)
    traffic_congestion = st.slider("Traffic Congestion Level (1-5)", min_value=1, max_value=5, value=3)
    weather_condition = st.slider("Weather Condition Score (1-4)", min_value=1, max_value=4, value=2)
    delivery_slot = st.slider("Delivery Slot (e.g., Morning/Afternoon/Evening shift represented as 1-3)", min_value=1, max_value=3, value=2)
    driver_experience = st.number_input("Driver Experience (years)", min_value=0, max_value=50, value=5)
    num_stops = st.number_input("Number of Stops", min_value=0, max_value=20, value=3)

with col2:
    vehicle_age = st.number_input("Vehicle Age (years)", min_value=0, max_value=30, value=3)
    road_condition_score = st.slider("Road Condition Score (1-5)", min_value=1, max_value=5, value=3)
    package_weight = st.number_input("Package Weight (kg)", min_value=0.0, value=15.0, step=0.5)
    fuel_efficiency = st.number_input("Fuel Efficiency (mpg)", min_value=0.0, value=15.0, step=0.5)
    warehouse_processing_time = st.number_input("Warehouse Processing Time (mins)", min_value=0, value=30, step=5)

# Build user input DataFrame
input_data = pd.DataFrame({
    'Delivery_Distance': [delivery_distance],
    'Traffic_Congestion': [traffic_congestion],
    'Weather_Condition': [weather_condition],
    'Delivery_Slot': [delivery_slot],
    'Driver_Experience': [driver_experience],
    'Num_Stops': [num_stops],
    'Vehicle_Age': [vehicle_age],
    'Road_Condition_Score': [road_condition_score],
    'Package_Weight': [package_weight],
    'Fuel_Efficiency': [fuel_efficiency],
    'Warehouse_Processing_Time': [warehouse_processing_time]
})

st.markdown("--- ")

# Predict delay status when button is clicked
if st.button("🔮 Predict Delivery Status"):
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("⚠️ Warning: The delivery is predicted to be **DELAYED**.")
    else:
        st.success("✅ Great news! The delivery is predicted to be **ON TIME**.")
