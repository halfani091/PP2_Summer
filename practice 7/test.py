import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="phonebook_db",
        user="postgres",
        password="KBTU0942#"
    )
    print("Connected successfully!")
    conn.close()
except Exception as e:
    print(type(e))
    print(e)