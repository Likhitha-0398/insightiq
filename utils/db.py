import sqlite3
import pandas as pd

DB_PATH = "database/insightiq.db"

def run_query(sql: str) -> pd.DataFrame:
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df