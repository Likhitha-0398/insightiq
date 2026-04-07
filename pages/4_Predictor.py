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
# on first run it may still be training in app.py
if not os.path.exists('database/delay_model.pkl'):
    st.warning("⏳ Model is still being prepared. Please go to the Homepage first, wait 2-3 minutes, then come back here.")
    st.stop()

# loading the pre-trained Random Forest model saved during initial setup
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

    # input must match the same feature order used during training
    X = np.array([[estimated_days, payment_value, freight_value, price]])

    prob = model.predict_proba(X)[0][1]  # probability of being late

    # scaling up raw probability since only 8.2% of orders are late in the dataset
    # this makes the predictor more sensitive to genuine risk signals
    adjusted_prob = min(prob * 3, 0.99)

    # orders with long delivery windows AND high freight are strong delay indicators
    if estimated_days >= 40 and freight_value >= 100:
        adjusted_prob = max(adjusted_prob, 0.45)

    if adjusted_prob >= 0.35:
        st.error(f"⚠️ HIGH RISK of late delivery — {adjusted_prob:.0%} probability of delay")
        st.markdown("""
        **Recommendations:**
        - Alert the seller to prioritize this order
        - Consider upgrading shipping method
        - Notify customer of potential delay
        """)
    else:
        st.success(f"✅ LOW RISK — {1-adjusted_prob:.0%} probability of on-time delivery")
        st.markdown("""
        **Good news!**
        - This order is likely to arrive on time
        - No special action required
        """)