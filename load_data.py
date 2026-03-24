import pandas as pd
import sqlite3
import os

RAW_DATA_PATH = "data/raw/"
DB_PATH = "database/insightiq.db"

os.makedirs("database", exist_ok=True)

files = {
    "orders":       "olist_orders_dataset.csv",
    "order_items":  "olist_order_items_dataset.csv",
    "payments":     "olist_order_payments_dataset.csv",
    "reviews":      "olist_order_reviews_dataset.csv",
    "customers":    "olist_customers_dataset.csv",
    "sellers":      "olist_sellers_dataset.csv",
    "products":     "olist_products_dataset.csv",
    "geolocation":  "olist_geolocation_dataset.csv",
    "translations": "product_category_name_translation.csv",
}

conn = sqlite3.connect(DB_PATH)

for table_name, filename in files.items():
    filepath = os.path.join(RAW_DATA_PATH, filename)
    df = pd.read_csv(filepath)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"✅ Loaded {table_name} — {len(df):,} rows")

conn.close()
print("\n🎉 Database ready at:", DB_PATH)