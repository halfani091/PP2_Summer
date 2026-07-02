import csv
import psycopg2
from connect import get_connection, init_db


# ---------- CREATE ----------

def insert_from_csv(filepath: str):
    """Bulk-insert contacts from a CSV file with columns:
    first_name,last_name,phone
    """
    conn = get_connection()
    inserted = 0
    try:
        with open(filepath, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = [
                (row["first_name"], row.get("last_name") or None, row["phone"])
                for row in reader
            ]

        with conn:
            with conn.cursor() as cur:
                # executemany for batch insert; ON CONFLICT avoids crashing on duplicate phones
                cur.executemany(
                    """
                    INSERT INTO contacts (first_name, last_name, phone)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (phone) DO NOTHING;
                    """,
                    rows,
                )
                inserted = cur.rowcount
        print(f"Imported rows from {filepath} (attempted: {len(rows)}).")
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except psycopg2.Error as e:
        print(f"Database error during CSV import: {e}")
    finally:
        conn.close()


def insert_from_console():
    """Ask the user for contact details and insert a single row."""
    first_name = input("First name: ").strip()
    last_name = input("Last name (optional): ").strip() or None
    phone = input("Phone: ").strip()

    if not first_name or not phone:
        print("First name and phone are required.")
        return

    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO contacts (first_name, last_name, phone)
                    VALUES (%s, %s, %s);
                    """,
                    (first_name, last_name, phone),
                )
        print("Contact added.")
    except psycopg2.errors.UniqueViolation:
        print("A contact with this phone number already exists.")
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


# ---------- READ ----------

def search_contacts():
    """Search contacts by name substring and/or phone prefix."""
    name_part = input("Name contains (leave empty to skip): ").strip()
    phone_prefix = input("Phone starts with (leave empty to skip): ").strip()

    conditions = []
    params = []

    if name_part:
        conditions.append("(first_name ILIKE %s OR last_name ILIKE %s)")
        params.extend([f"%{name_part}%", f"%{name_part}%"])

    if phone_prefix:
        conditions.append("phone LIKE %s")
        params.append(f"{phone_prefix}%")

    where_clause = f"WHERE {' AND '.join(conditions)}" if conditions else ""
    query = f"""
        SELECT id, first_name, last_name, phone
        FROM contacts
        {where_clause}
        ORDER BY first_name;
    """

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            rows = cur.fetchall()

        if not rows:
            print("No contacts found.")
            return

        print(f"{'ID':<5}{'First name':<15}{'Last name':<15}{'Phone':<20}")
        for row in rows:
            id_, fn, ln, phone = row
            print(f"{id_:<5}{fn:<15}{(ln or ''):<15}{phone:<20}")
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


# ---------- UPDATE ----------

def update_contact():
    """Update first name or phone for a contact identified by current phone."""
    current_phone = input("Phone of the contact to update: ").strip()

    field = input("Update (1) first name or (2) phone? Enter 1 or 2: ").strip()
    if field == "1":
        new_value = input("New first name: ").strip()
        column = "first_name"
    elif field == "2":
        new_value = input("New phone: ").strip()
        column = "phone"
    else:
        print("Invalid choice.")
        return

    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    f"UPDATE contacts SET {column} = %s WHERE phone = %s;",
                    (new_value, current_phone),
                )
                if cur.rowcount == 0:
                    print("No contact found with that phone number.")
                else:
                    print("Contact updated.")
    except psycopg2.errors.UniqueViolation:
        print("That phone number is already taken by another contact.")
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


# ---------- DELETE ----------

def delete_contact():
    """Delete a contact by username (first name) or phone number."""
    key = input("Delete by (1) first name or (2) phone? Enter 1 or 2: ").strip()
    if key == "1":
        value = input("First name to delete: ").strip()
        column = "first_name"
    elif key == "2":
        value = input("Phone to delete: ").strip()
        column = "phone"
    else:
        print("Invalid choice.")
        return

    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(f"DELETE FROM contacts WHERE {column} = %s;", (value,))
                if cur.rowcount == 0:
                    print("No matching contact found.")
                else:
                    print(f"Deleted {cur.rowcount} contact(s).")
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


# ---------- MENU ----------

MENU = """
==== PhoneBook ====
1. Import contacts from CSV
2. Add contact from console
4. Update contact
5. Delete contact
0. Exit
"""


def main():
    init_db()
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            path = input("CSV file path (default contacts.csv): ").strip() or "contacts.csv"
            insert_from_csv(path)
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
