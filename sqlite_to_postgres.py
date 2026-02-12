import sqlite3
import pandas as pd
from sqlalchemy import create_engine

# ---------- CONFIG ----------
SQLITE_DB = "database.db"
POSTGRES_URL = "postgresql://hrleave_db_user:HUrl5S7Wb0JcW0Hi1qvPbhAw8jxMjheO@dpg-d65thqfgi27c73a56it0-a.singapore-postgres.render.com/hrleave_db"
# ----------------------------

# Connect SQLite
sqlite_conn = sqlite3.connect(SQLITE_DB)

# Connect PostgreSQL
pg_engine = create_engine(POSTGRES_URL)

# Tables to migrate (ORDER MATTERS)
tables = [
    "users",
    "departments",
    "holidays",
    "leave_applications",
    "leaves",
    "leave_logs",
    "mc_records",
    "settings"
]

for table in tables:
    print(f"Migrating {table}...")
    df = pd.read_sql_query(f"SELECT * FROM {table}", sqlite_conn)

    df.to_sql(
        table,
        pg_engine,
        if_exists="append",
        index=False
    )

print("✅ Migration completed successfully")
