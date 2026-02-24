import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ======================================
# Load Model
# ======================================
model = joblib.load("final_random_forest_model.pkl")

# ======================================
# Load Dataset (For Dropdown Values)
# ======================================
df = pd.read_csv("cars24_20221210.csv")

st.set_page_config(page_title="Used Car Price Predictor", page_icon="🚗")

st.title("🚗 Used Car Price Prediction")
st.markdown("Select the car details below to estimate resale value.")

# ======================================
# Prepare Dropdown Values
# ======================================
brands = sorted(df["make"].dropna().unique())
fueltypes = sorted(df["fueltype"].dropna().unique())
bodytypes = sorted(df["bodytype"].dropna().unique())
states = sorted(df["registrationstate"].dropna().unique())

# ======================================
# Layout
# ======================================
col1, col2 = st.columns(2)

with col1:
    make = st.selectbox("Brand", brands)
    fueltype = st.selectbox("Fuel Type", fueltypes)
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
    bodytype = st.selectbox("Body Type", bodytypes)

with col2:
    year = st.number_input("Manufacturing Year", 2000, 2026, 2020)
    kilometerdriven = st.number_input("Kilometers Driven", 0, 300000, 30000)
    ownernumber = st.selectbox("Owner Number", [1, 2, 3, 4, 5])
    isc24assured = st.selectbox("C24 Assured", ["Yes", "No"])
    
    registrationstate = st.selectbox("Registration State", states)
    
    # Filter cities based on selected state
    filtered_cities = sorted(
        df[df["registrationstate"] == registrationstate]["city"]
        .dropna()
        .unique()
    )
    
    city = st.selectbox("City", filtered_cities)

# ======================================
# Predict Button
# ======================================
if st.button("Predict Price"):
    
    isc24_value = 1 if isc24assured == "Yes" else 0

    input_df = pd.DataFrame({
        "make": [make],
        "fueltype": [fueltype],
        "transmission": [transmission],
        "bodytype": [bodytype],
        "year": [year],
        "kilometerdriven": [kilometerdriven],
        "ownernumber": [ownernumber],
        "isc24assured": [isc24_value],
        "registrationstate": [registrationstate],
        "city": [city]
    })

    log_prediction = model.predict(input_df)[0]
    predicted_price = np.expm1(log_prediction)

    st.success(f"💰 Estimated Car Price: ₹ {predicted_price:,.2f}")

    # Optional: Show Price Range
    lower = predicted_price * 0.9
    upper = predicted_price * 1.1

    st.info(f"📊 Expected Price Range: ₹ {lower:,.0f} - ₹ {upper:,.0f}")