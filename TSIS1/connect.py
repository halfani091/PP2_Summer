import os
import psycopg2
from psycopg2 import OperationalError
from config import DB_CONFIG

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except OperationalError as e:
        print(f"Could not connect to the database: {e}")
        raise


def _run_sql_file(conn, filename: str):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        sql = f.read()
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql)


def init_db():
    """Creates/updates the schema (contacts, groups, phones) and
    (re)installs the TSIS1 stored procedures/functions."""
    conn = get_connection()
    try:
        _run_sql_file(conn, "schema.sql")
        _run_sql_file(conn, "procedures.sql")
        print("Schema and procedures are ready.")
    finally:
        conn.close()


if __name__ == "__main__":
    init_db()
