import streamlit as st
from utils.styles import apply_styles
apply_styles()
import os
import sys
sys.path.append('.')

# Auto-build database if it doesn't exist
if not os.path.exists('database/insightiq.db'):
    import pandas as pd
    import sqlite3
    os.makedirs("database", exist_ok=True)
    files = {
        "orders":       "data/raw/olist_orders_dataset.csv",
        "order_items":  "data/raw/olist_order_items_dataset.csv",
        "payments":     "data/raw/olist_order_payments_dataset.csv",
        "reviews":      "data/raw/olist_order_reviews_dataset.csv",
        "customers":    "data/raw/olist_customers_dataset.csv",
        "sellers":      "data/raw/olist_sellers_dataset.csv",
        "products":     "data/raw/olist_products_dataset.csv",
        "geolocation":  "data/raw/olist_geolocation_dataset.csv",
        "translations": "data/raw/product_category_name_translation.csv",
    }
    conn = sqlite3.connect('database/insightiq.db')
    for table_name, filepath in files.items():
        df = pd.read_csv(filepath)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

# Auto-train model if it doesn't exist
if not os.path.exists('database/delay_model.pkl'):
    import pandas as pd
    import sqlite3
    import pickle
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split

    conn = sqlite3.connect('database/insightiq.db')
    df = pd.read_sql_query('''
        SELECT
            julianday(o.order_estimated_delivery_date)
              - julianday(o.order_purchase_timestamp) as estimated_days,
            julianday(o.order_delivered_customer_date)
              - julianday(o.order_purchase_timestamp) as actual_days,
            p.payment_value,
            i.freight_value,
            i.price
        FROM orders o
        JOIN payments p ON o.order_id = p.order_id
        JOIN order_items i ON o.order_id = i.order_id
        WHERE o.order_delivered_customer_date IS NOT NULL
        AND o.order_estimated_delivery_date IS NOT NULL
    ''', conn)
    conn.close()
    df = df.dropna()
    df['late'] = (df['actual_days'] > df['estimated_days']).astype(int)
    features = ['estimated_days', 'payment_value', 'freight_value', 'price']
    X = df[features]
    y = df['late']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(
        n_estimators=100, class_weight='balanced', random_state=42)
    model.fit(X_train, y_train)
    with open('database/delay_model.pkl', 'wb') as f:
        pickle.dump(model, f)

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