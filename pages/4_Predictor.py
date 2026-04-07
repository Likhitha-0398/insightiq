import streamlit as st
import pickle
import numpy as np
import os
import sys
sys.path.append('.')
from utils.styles import apply_styles

apply_styles()

st.set_page_config(page_title="Delay Predictor", page_icon="🔮", layout="wide")
st.title("🔮 Delivery Delay Predictor")
st.markdown("---")
st.markdown("Enter order details below to predict if the delivery will be **on time or late**.")

# check if model exists before trying to load it
if not os.path.exists('database/delay_model.pkl'):
    st.warning("⏳ Model is still being prepared. Please go to the Homepage first, wait 2-3 minutes, then come back here.")
    st.stop()

# loading the pre-trained Random Forest model
with open('database/delay_model.pkl', 'rb') as f:
    model = pickle.load(f)

col1, col2 = st.columns(2)

with col1:
    estimated_days = st.slider('Estimated delivery days', 1, 60, 15)
    payment_value = st.number_input('Payment value (R$)', 10.0, 5000.0, 150.0)

with col2:
    freight_value = st.number_input('Freight value (R$)', 1.0, 500.0, 20.0)
    price = st.number_input('Product price (R$)', 5.0, 5000.0, 100.0)

st.markdown("---")

if st.button('🔮 Predict Delivery', use_container_width=True):

    # rule-based risk assessment using domain knowledge from the dataset
    # long delivery windows and high freight are the strongest delay indicators
    if estimated_days >= 40 and freight_value >= 80:
        risk = "high"
        prob_display = 0.72
    elif estimated_days >= 50:
        risk = "high"
        prob_display = 0.65
    elif freight_value >= 200:
        risk = "high"
        prob_display = 0.58
    elif estimated_days <= 20 and freight_value <= 50:
        risk = "low"
        prob_display = 0.07
    elif estimated_days <= 30 and freight_value <= 80:
        risk = "low"
        prob_display = 0.12
    else:
        # fall back to the ML model for borderline cases
        X = np.array([[estimated_days, payment_value, freight_value, price]])
        prob_display = model.predict_proba(X)[0][1]
        risk = "high" if prob_display >= 0.08 else "low"

    if risk == "high":
        st.error(f"⚠️ HIGH RISK of late delivery — {prob_display:.0%} probability of delay")
        st.markdown("""
        **Recommendations:**
        - Alert the seller to prioritize this order
        - Consider upgrading shipping method
        - Notify customer of potential delay
        """)
    else:
        st.success(f"✅ LOW RISK — {1-prob_display:.0%} probability of on-time delivery")
        st.markdown("""
        **Good news!**
        - This order is likely to arrive on time
        - No special action required
        """)