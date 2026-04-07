import streamlit as st
import os
import sys
sys.path.append('.')
from utils.styles import apply_styles

# Main entry point for the InsightIQ dashboard.
# Keeping setup automatic so the app runs without manual database/model creation.
apply_styles()

# If the database doesn't exist, build it from raw CSV files
if True:  # always retrain to use latest model settings
    import pandas as pd
    import sqlite3

    os.makedirs("database", exist_ok=True)

    # Mapping dataset files to table names to recreate a relational structure
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

    # Loading each dataset and storing it into SQLite
    # This converts raw CSVs into a queryable database
    for table_name, filepath in files.items():
        df = pd.read_csv(filepath)
        df.to_sql(table_name, conn, if_exists="replace", index=False)

    conn.close()

# If the trained model doesn't exist, train it automatically
if not os.path.exists('database/delay_model.pkl'):
    import pandas as pd
    import sqlite3
    import pickle
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split

    conn = sqlite3.connect('database/insightiq.db')

    # Extracting relevant features by joining multiple tables
    # Combining order, payment, and item data to understand delivery behavior
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

    # Defining delay: 1 = late delivery, 0 = on-time or early
    df['late'] = (df['actual_days'] > df['estimated_days']).astype(int)

    features = ['estimated_days', 'payment_value', 'freight_value', 'price']
    X = df[features]
    y = df['late']

    # Splitting data to check how well the model generalizes
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Using Random Forest since it handles non-linear relationships well
    model = RandomForestClassifier(
        n_estimators=100, class_weight='balanced', random_state=42)

    model.fit(X_train, y_train)

    # Saving model so we don’t retrain every time
    with open('database/delay_model.pkl', 'wb') as f:
        pickle.dump(model, f)

st.set_page_config(
    page_title="InsightIQ",
    page_icon="📊",
    layout="wide"
)

st.title("📊 InsightIQ")
st.subheader("E-Commerce Analytics Dashboard with Predictive Insights")
st.markdown("---")

# Displaying key business metrics for quick overview
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

# Keeping the interface simple so users can explore insights easily
st.info("Select a page from the left sidebar to begin exploring.")