import streamlit as st
import pickle
import numpy as np
import pandas as pd

# ---------- Load model ----------
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# ---------- Page setup ----------
st.set_page_config(page_title="Startup Profit Predictor", page_icon="💼", layout="centered")

# ---------- Massive UI with gradient & glass effect ----------
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
<style>
  html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif !important;
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 40%, #334155 100%);
    color: #e2e8f0;
  }
  .block-container {
    max-width: 900px !important;
    padding-top: 2rem;
  }
  .title {
    font-size: 2.4rem;
    font-weight: 700;
    background: linear-gradient(90deg, #60a5fa, #a78bfa, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .card {
    background: rgba(255, 255, 255, 0.06);
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
  }
  .stButton>button {
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white;
    font-weight: 700;
    font-size: 1rem;
    border-radius: 12px;
    width: 100%;
    height: 3rem;
    border: none;
    box-shadow: 0 4px 15px rgba(99, 102, 241, .4);
    transition: 0.3s;
  }
  .stButton>button:hover {
    transform: scale(1.02);
    box-shadow: 0 8px 25px rgba(139, 92, 246, .5);
  }
  .profit-box {
    text-align: center;
    padding: 20px;
    margin-top: 15px;
    border-radius: 12px;
    background: linear-gradient(120deg, #22c55e33, #16a34a33);
    border: 1px solid #16a34a55;
    color: #bbf7d0;
    font-size: 1.2rem;
    font-weight: 700;
  }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">💼 Startup Profit Predictor</p>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)

# ---------- Inputs ----------
rd = st.number_input("R&D Spend (in ₹ thousands)", min_value=0.0, step=10.0)
admin = st.number_input("Administration (in ₹ thousands)", min_value=0.0, step=10.0)
marketing = st.number_input("Marketing Spend (in ₹ thousands)", min_value=0.0, step=10.0)
state = st.selectbox("Select State", ("New York", "California", "Florida"))

st.caption("💡 Enter values in **thousands**. Example: for ₹1,50,000 → enter 150. Model auto-scales inputs to match training data.")

# ---------- Encode 3 dummy variables (6 total features) ----------
state_newyork = 1 if state == "New York" else 0
state_california = 1 if state == "California" else 0
state_florida = 1 if state == "Florida" else 0

# ---------- Prediction ----------
if st.button("Predict Profit 💰"):
    # Scale inputs to realistic dataset range
    X = np.array([[rd * 1000, admin * 1000, marketing * 1000,
                   state_newyork, state_california, state_florida]])

    prediction = model.predict(X)[0]
    profit_rupees = prediction  # model outputs already in ₹ if trained that way

    # Beautify output
    st.markdown(f'<div class="profit-box">Estimated Profit: ₹{profit_rupees:,.2f}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
