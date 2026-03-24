import streamlit as st

st.set_page_config(
    page_title="InsightIQ",
    page_icon="📊",
    layout="wide"
)

st.title("📊 InsightIQ")
st.subheader("AI-Powered E-Commerce Analytics Dashboard")
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Orders", "99,441")
col2.metric("Total Revenue", "R$ 13.6M")
col3.metric("Avg Delivery Days", "12.5")
col4.metric("Avg Review Score", "4.07 / 5")

st.markdown("---")
st.markdown("""
Welcome to **InsightIQ** — an intelligent BI platform built on the
Olist Brazilian E-Commerce dataset (100K real orders, 2016-2018).

👈 Use the sidebar to navigate between pages.
""")

st.info("Select a page from the left sidebar to begin exploring.")