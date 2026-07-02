import psycopg2
from psycopg2 import OperationalError
from config import DB_CONFIG


def get_connection():
    """Create and return a new database connection."""
    try:
        print(DB_CONFIG)
        print(repr(DB_CONFIG))
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except OperationalError as e:
        print(f"Could not connect to the database: {e}")
        raise


def init_db():
    """Create the contacts table if it doesn't exist yet."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50),
        phone VARCHAR(20) NOT NULL UNIQUE
    );
    """
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(create_table_sql)
        print("Table 'contacts' is ready.")
    finally:
        conn.close()


if __name__ == "__main__":
    init_db()
