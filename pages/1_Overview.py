import streamlit as st
import plotly.express as px
from utils.styles import apply_styles
apply_styles()
import sys
sys.path.append('.')
from utils.db import run_query

st.set_page_config(page_title="Overview", page_icon="📈", layout="wide")
st.title("📈 Business Overview")
st.markdown("---")

df = run_query('''
    SELECT strftime('%Y-%m', order_purchase_timestamp) as month,
           COUNT(*) as total_orders,
           ROUND(SUM(payment_value), 2) as revenue
    FROM orders o
    JOIN payments p ON o.order_id = p.order_id
    WHERE order_purchase_timestamp IS NOT NULL
    GROUP BY month ORDER BY month
''')

col1, col2 = st.columns(2)

with col1:
    fig = px.line(df, x='month', y='revenue',
        title='Monthly Revenue (R$)',
        labels={'month': 'Month', 'revenue': 'Revenue (R$)'})
    fig.update_traces(line_color='#2E75B6', line_width=2)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig2 = px.bar(df, x='month', y='total_orders',
        title='Monthly Order Volume',
        labels={'month': 'Month', 'total_orders': 'Orders'},
        color_discrete_sequence=['#1D9E75'])
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("### Key Insights")
col3, col4, col5 = st.columns(3)
col3.metric("Peak Revenue Month", "Nov 2017")
col4.metric("Best Order Month", "Nov 2017")
col5.metric("Avg Monthly Revenue", "R$ 1.04M")