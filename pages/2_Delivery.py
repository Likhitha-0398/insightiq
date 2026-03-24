import streamlit as st
import plotly.express as px
import sys
sys.path.append('.')
from utils.db import run_query

st.set_page_config(page_title="Delivery", page_icon="🚚", layout="wide")
st.title("🚚 Delivery Performance")
st.markdown("---")

df = run_query('''
    SELECT
        ROUND(julianday(order_delivered_customer_date)
             - julianday(order_purchase_timestamp), 0) as delivery_days
    FROM orders
    WHERE order_delivered_customer_date IS NOT NULL
    AND order_purchase_timestamp IS NOT NULL
''')

col1, col2, col3 = st.columns(3)
col1.metric("Avg Delivery Time", f"{df['delivery_days'].mean():.1f} days")
col2.metric("Fastest Delivery", f"{df['delivery_days'].min():.0f} days")
col3.metric("Slowest Delivery", f"{df['delivery_days'].max():.0f} days")

st.markdown("---")

fig = px.histogram(df, x='delivery_days',
    title='Distribution of Delivery Times',
    labels={'delivery_days': 'Days to Deliver'},
    nbins=50,
    color_discrete_sequence=['#2E75B6'])
fig.update_layout(bargap=0.1)
st.plotly_chart(fig, use_container_width=True)

st.markdown("### Key Observations")
st.markdown("""
- Most orders are delivered within **10-15 days**
- A small percentage of orders take over **30 days**
- Delivery time is the **#1 driver of customer dissatisfaction**
""")