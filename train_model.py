import pandas as pd
import sqlite3
import pickle
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

conn = sqlite3.connect('database/insightiq.db')

# Joining orders, payments and items to get features that influence delivery time
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

# 1 = late, 0 = on time — this is what the model learns to predict
df['late'] = (df['actual_days'] > df['estimated_days']).astype(int)

features = ['estimated_days', 'payment_value', 'freight_value', 'price']
X = df[features]
y = df['late']

# fixed random state so results are reproducible every run
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# balanced weight helps the model handle the class imbalance
# only ~8% of orders are late so without this it would just predict on-time always
model = RandomForestClassifier(
    n_estimators=200,
    class_weight={0: 1, 1: 8},
    random_state=42,
    min_samples_leaf=3,
    max_depth=18
)
model.fit(X_train, y_train)

acc = accuracy_score(y_test, model.predict(X_test))
print(f"✅ Model accuracy: {acc:.2%}")
print("\n📊 Classification Report:")
print(classification_report(y_test, model.predict(X_test)))

# saving the trained model so the dashboard loads it instantly without retraining
os.makedirs("database", exist_ok=True)
with open('database/delay_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("\n🎉 Model saved to database/delay_model.pkl")