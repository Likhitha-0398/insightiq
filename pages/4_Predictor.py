import streamlit as st
import pickle
import numpy as np
import sys
sys.path.append('.')

st.set_page_config(page_title="Delay Predictor", page_icon="🔮", layout="wide")
st.title("🔮 Delivery Delay Predictor")
st.markdown("---")
st.markdown("Enter order details below to predict if the delivery will be **on time or late**.")

with open('database/delay_model.pkl', 'rb') as f:
    model = pickle.load(f)

col1, col2 = st.columns(2)

with col1:
    estimated_days = st.slider(
        'Estimated delivery days', 1, 60, 15)
    payment_value = st.number_input(
        'Payment value (R$)', 10.0, 5000.0, 150.0)

with col2:
    freight_value = st.number_input(
        'Freight value (R$)', 1.0, 500.0, 20.0)
    price = st.number_input(
        'Product price (R$)', 5.0, 5000.0, 100.0)

st.markdown("---")

if st.button('🔮 Predict Delivery', use_container_width=True):
    X = np.array([[estimated_days, payment_value, freight_value, price]])
    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0][1]

    if pred == 1:
        st.error(f"⚠️ HIGH RISK of late delivery — {prob:.0%} probability of delay")
        st.markdown("""
        **Recommendations:**
        - Alert the seller to prioritize this order
        - Consider upgrading shipping method
        - Notify customer of potential delay
        """)
    else:
        st.success(f"✅ LOW RISK — {1-prob:.0%} probability of on-time delivery")
        st.markdown("""
        **Good news!**
        - This order is likely to arrive on time
        - No special action required
        """)