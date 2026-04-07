import sqlite3
import pandas as pd

# keeping the db path in one place so it's easy to change later
DB_PATH = "database/insightiq.db"

def run_query(sql: str) -> pd.DataFrame:
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(sql, conn)
    conn.close()  # always close after querying to avoid memory issues
    return df