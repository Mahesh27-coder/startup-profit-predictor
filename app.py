import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.title("💼 Startup Profit Predictor")

st.markdown("""
<style>
    body {
        background-color: #f0f4f8;
        color: #333333;
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton>button {
        background-color: #0078D7;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 10em;
        font-size: 16px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #005a9e;
    }
</style>
""", unsafe_allow_html=True)

st.header("Enter the following startup details:")

# Input fields
rd = st.number_input("R&D Spend", min_value=0.0, step=1000.0)
admin = st.number_input("Administration", min_value=0.0, step=1000.0)
marketing = st.number_input("Marketing Spend", min_value=0.0, step=1000.0)
state = st.selectbox("State", ("New York", "California", "Florida"))

# One-hot encoding for state
state_newyork = 1 if state == "New York" else 0
state_california = 1 if state == "California" else 0
state_florida = 1 if state == "Florida" else 0

# Predict button
if st.button("Predict Profit"):
    # Arrange input data in same order used during training
    input_data = np.array([[rd, admin, marketing, state_newyork, state_california, state_florida]])
    
    # Predict
    prediction = model.predict(input_data)
    
    # Display result
    st.success(f"💰 Predicted Profit: ${prediction[0]:,.2f}")
