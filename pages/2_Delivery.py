import streamlit as st
import plotly.express as px
import sys
sys.path.append('.')
from utils.styles import apply_styles
from utils.db import run_query

apply_styles()

st.set_page_config(page_title="Delivery", page_icon="🚚", layout="wide")
st.title("🚚 Delivery Performance")
st.markdown("---")

# Calculating delivery duration by comparing purchase and delivery timestamps
# helps understand how long orders actually take to reach customers
df = run_query('''
    SELECT
        ROUND(julianday(order_delivered_customer_date)
             - julianday(order_purchase_timestamp), 0) as delivery_days
    FROM orders
    WHERE order_delivered_customer_date IS NOT NULL
    AND order_purchase_timestamp IS NOT NULL
''')

# quick summary metrics at the top for fast interpretation
col1, col2, col3 = st.columns(3)
col1.metric("Avg Delivery Time", f"{df['delivery_days'].mean():.1f} days")
col2.metric("Fastest Delivery", f"{df['delivery_days'].min():.0f} days")
col3.metric("Slowest Delivery", f"{df['delivery_days'].max():.0f} days")

st.markdown("---")

# histogram shows the spread of delivery times across all orders
# makes it easy to spot where most deliveries fall and identify outliers
fig = px.histogram(df, x='delivery_days',
    title='Distribution of Delivery Times',
    labels={'delivery_days': 'Days to Deliver'},
    nbins=50,
    color_discrete_sequence=['#2E75B6'])
fig.update_layout(bargap=0.1)
st.plotly_chart(fig, use_container_width=True)

st.markdown("### Key Observations")
st.markdown("""
- Most orders are delivered within **10–15 days**
- A smaller portion of orders take significantly longer (30+ days)
- Longer delivery times tend to impact customer satisfaction
""")