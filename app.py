import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open("realestate_model.pkl", "rb"))

# Streamlit app layout
st.set_page_config(page_title="Real Estate Price Predictor", layout="centered")

st.title("🏠 Real Estate Price Predictor")
st.markdown("Predict house price based on features like rooms, area, parking, etc.")

# User inputs
rooms = st.number_input("Number of Rooms", min_value=1, max_value=10, value=3)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=2)
area_sqft = st.number_input("Area (sqft)", min_value=300, max_value=10000, value=1200)
parking = st.number_input("Number of Parking Spaces", min_value=0, max_value=5, value=1)
price_per_sqft = st.number_input("Price per Sqft (₹)", min_value=1000, max_value=20000, value=5000)

# Prediction
if st.button("Predict Price"):
    input_data = np.array([[rooms, bedrooms, area_sqft, parking, price_per_sqft]])
    predicted_price = model.predict(input_data)[0]
    st.success(f"🏷️ Estimated House Price: ₹ {predicted_price:,.2f}")
