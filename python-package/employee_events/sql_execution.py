from sqlite3 import connect
from pathlib import Path
import pandas as pd

# Absolute path to the SQLite database
db_path = Path(__file__).resolve().parent / "employee_events.db"


class QueryMixin:
    def pandas_query(self, sql_query: str) -> pd.DataFrame:
        conn = connect(db_path)
        df = pd.read_sql_query(sql_query, conn)
        conn.close()
        return df

    def query(self, sql_query: str):
        conn = connect(db_path)
        cur = conn.cursor()
        result = cur.execute(sql_query).fetchall()
        conn.close()
        return result
