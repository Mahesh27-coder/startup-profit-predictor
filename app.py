import streamlit as st
import pickle
import numpy as np

# -----------------------------
# Load the trained model
# -----------------------------
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# -----------------------------
# App UI
# -----------------------------
st.set_page_config(page_title="Startup Profit Predictor", page_icon="💼", layout="centered")
st.title("💼 Startup Profit Predictor")

st.markdown("""
<style>
    body {
        background-color: #f4f6fa;
        color: #333;
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

st.subheader("Enter Startup Details:")

# -----------------------------
# Input Fields
# -----------------------------
rd = st.number_input("R&D Spend ($)", min_value=0.0, step=1000.0)
admin = st.number_input("Administration ($)", min_value=0.0, step=1000.0)
marketing = st.number_input("Marketing Spend ($)", min_value=0.0, step=1000.0)
state = st.selectbox("Select State", ("New York", "California", "Florida"))

# -----------------------------
# One-hot encoding (drop_first=True → 2 columns only)
# -----------------------------
if state == "New York":
    state_california, state_florida = 0, 0
elif state == "California":
    state_california, state_florida = 1, 0
else:  # Florida
    state_california, state_florida = 0, 1

# -----------------------------
# Predict button
# -----------------------------
if st.button("Predict Profit 💰"):
    # Order: [R&D, Admin, Marketing, State_California, State_Florida]
    x = np.array([[rd, admin, marketing, state_california, state_florida]])
    prediction = model.predict(x)
    st.success(f"Predicted Profit: ${prediction[0]:,.2f}")
