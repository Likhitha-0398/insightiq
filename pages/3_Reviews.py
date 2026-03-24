import streamlit as st
import plotly.express as px
import sys
sys.path.append('.')
from utils.db import run_query

st.set_page_config(page_title="Reviews", page_icon="⭐", layout="wide")
st.title("⭐ Customer Reviews")
st.markdown("---")

df = run_query('''
    SELECT review_score, COUNT(*) as count
    FROM reviews
    GROUP BY review_score
    ORDER BY review_score
''')

avg = run_query('SELECT ROUND(AVG(review_score), 2) as avg FROM reviews')
total = run_query('SELECT COUNT(*) as total FROM reviews')
five_star = run_query('SELECT COUNT(*) as total FROM reviews WHERE review_score = 5')

col1, col2, col3 = st.columns(3)
col1.metric("Avg Review Score", f"{avg['avg'][0]} / 5")
col2.metric("Total Reviews", f"{total['total'][0]:,}")
col3.metric("5 Star Reviews", f"{five_star['total'][0]:,}")

st.markdown("---")

fig = px.bar(df, x='review_score', y='count',
    title='Review Score Distribution',
    labels={'review_score': 'Score (1-5)', 'count': 'Number of Reviews'},
    color='review_score',
    color_continuous_scale='RdYlGn')
fig.update_layout(showlegend=False)
st.plotly_chart(fig, use_container_width=True)

st.markdown("### Key Observations")
st.markdown("""
- **57.8%** of customers gave a 5-star rating
- **11.5%** of customers gave a 1-star rating
- Low scores are strongly linked to **late deliveries**
""")