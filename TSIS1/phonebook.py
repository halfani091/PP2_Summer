import csv
import json
import datetime
import psycopg2
from connect import get_connection, init_db




def show_contacts():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts ORDER BY id")
    rows = cur.fetchall()
    print("\nPhoneBook:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]} {row[2] or ''}, Phone: {row[3]}")
    cur.close()
    conn.close()


def insert_from_csv(filepath: str):
    conn = get_connection()
    try:
        with open(filepath, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = [
                (row["first_name"], row.get("last_name") or None, row["phone"])
                for row in reader
            ]
        with conn:
            with conn.cursor() as cur:
                cur.executemany(
                    """
                    INSERT INTO contacts (first_name, last_name, phone)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (phone) DO NOTHING;
                    """,
                    rows,
                )
        print(f"Imported rows from {filepath} (attempted: {len(rows)}).")
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except psycopg2.Error as e:
        print(f"Database error during CSV import: {e}")
    finally:
        conn.close()


def insert_from_console():
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
                    "INSERT INTO contacts (first_name, last_name, phone) VALUES (%s, %s, %s);",
                    (first_name, last_name, phone),
                )
        print("Contact added.")
    except psycopg2.errors.UniqueViolation:
        print("A contact with this phone number already exists.")
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


def search_contacts():
    name_part = input("Name contains (leave empty to skip): ").strip()
    phone_prefix = input("Phone starts with (leave empty to skip): ").strip()

    conditions, params = [], []
    if name_part:
        conditions.append("""(
            first_name ILIKE %s
            OR last_name ILIKE %s
            OR (first_name || ' ' || last_name) ILIKE %s
        )""")
        params.extend([f"%{name_part}%", f"%{name_part}%", f"%{name_part}%"])
    if phone_prefix:
        conditions.append("phone LIKE %s")
        params.append(f"{phone_prefix}%")

    where_clause = f"WHERE {' AND '.join(conditions)}" if conditions else ""
    query = f"SELECT id, first_name, last_name, phone FROM contacts {where_clause} ORDER BY first_name;"

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            rows = cur.fetchall()
        if not rows:
            print("No contacts found.")
            return
        print(f"{'ID':<5}{'First name':<15}{'Last name':<15}{'Phone':<20}")
        for id_, fn, ln, phone in rows:
            print(f"{id_:<5}{fn:<15}{(ln or ''):<15}{phone:<20}")
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


def update_contact():
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
                cur.execute(f"UPDATE contacts SET {column} = %s WHERE phone = %s;", (new_value, current_phone))
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


def delete_contact():
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




def search_by_pattern_func():
    pattern = input("Введите фрагмент имени/фамилии/телефона: ").strip()
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_contacts_by_pattern(%s);", (pattern,))
            rows = cur.fetchall()
        if not rows:
            print("Ничего не найдено.")
            return
        print(f"{'ID':<5}{'First name':<15}{'Last name':<15}{'Phone':<20}")
        for id_, fn, ln, phone in rows:
            print(f"{id_:<5}{fn:<15}{(ln or ''):<15}{phone:<20}")
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


def _fetch_page(limit, offset):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
            return cur.fetchall()
    finally:
        conn.close()


def show_page_func():
    try:
        limit = int(input("Сколько записей на странице (limit): ").strip())
        offset = int(input("Сколько записей пропустить (offset): ").strip())
    except ValueError:
        print("Нужно вводить числа.")
        return
    try:
        rows = _fetch_page(limit, offset)
        if not rows:
            print("На этой странице записей нет.")
            return
        print(f"{'ID':<5}{'First name':<15}{'Last name':<15}{'Phone':<20}")
        for id_, fn, ln, phone in rows:
            print(f"{id_:<5}{fn:<15}{(ln or ''):<15}{phone:<20}")
    except psycopg2.Error as e:
        print(f"Database error: {e}")


def upsert_contact_proc():
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
                cur.execute("CALL upsert_contact(%s, %s, %s);", (first_name, last_name, phone))
        print("Contact upserted (added or updated).")
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


def insert_many_proc():
    n = input("Сколько контактов добавить: ").strip()
    if not n.isdigit() or int(n) <= 0:
        print("Нужно положительное число.")
        return
    n = int(n)
    first_names, last_names, phones = [], [], []
    for i in range(n):
        print(f"-- Контакт {i + 1} --")
        first_names.append(input("First name: ").strip())
        last_names.append(input("Last name (optional): ").strip() or None)
        phones.append(input("Phone: ").strip())

    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("CALL insert_many_contacts(%s, %s, %s);", (first_names, last_names, phones))
        for notice in conn.notices:
            print(notice.strip())
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


def delete_contact_proc():
    value = input("Введите first name или phone для удаления: ").strip()
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("CALL delete_contact_by(%s);", (value,))
        for notice in conn.notices:
            print(notice.strip())
        print("Готово.")
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


# ============================================================
# TSIS1 3.2 — Advanced console search & filter
# ============================================================

def show_full_contacts():
    """Extended view: email, birthday, group, and all phone numbers."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT c.id, c.first_name, c.last_name, c.phone, c.email, c.birthday,
                       g.name AS group_name, c.created_at,
                       COALESCE(string_agg(p.phone || ' (' || p.type || ')', ', '), '') AS extra_phones
                FROM contacts c
                LEFT JOIN groups g ON g.id = c.group_id
                LEFT JOIN phones p ON p.contact_id = c.id
                GROUP BY c.id, g.name
                ORDER BY c.id;
            """)
            rows = cur.fetchall()
        if not rows:
            print("No contacts found.")
            return
        for id_, fn, ln, phone, email, bday, group, created_at, extra_phones in rows:
            print(f"\nID: {id_}  {fn} {ln or ''}")
            print(f"  Phone: {phone}" + (f" | Other phones: {extra_phones}" if extra_phones else ""))
            print(f"  Email: {email or '-'}")
            print(f"  Birthday: {bday or '-'}")
            print(f"  Group: {group or '-'}")
            print(f"  Added: {created_at}")
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


def filter_by_group():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name FROM groups ORDER BY name;")
            groups = cur.fetchall()
            if not groups:
                print("No groups defined yet.")
                return
            print("Groups:")
            for gid, name in groups:
                print(f"  {gid}. {name}")
            choice = input("Enter group name to filter by: ").strip()

            cur.execute("""
                SELECT c.id, c.first_name, c.last_name, c.phone, c.email
                FROM contacts c
                JOIN groups g ON g.id = c.group_id
                WHERE g.name ILIKE %s
                ORDER BY c.first_name;
            """, (choice,))
            rows = cur.fetchall()
        if not rows:
            print("No contacts in that group.")
            return
        print(f"{'ID':<5}{'First name':<15}{'Last name':<15}{'Phone':<20}{'Email':<25}")
        for id_, fn, ln, phone, email in rows:
            print(f"{id_:<5}{fn:<15}{(ln or ''):<15}{phone:<20}{(email or ''):<25}")
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


def search_by_email():
    fragment = input("Email contains (e.g. 'gmail'): ").strip()
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, first_name, last_name, email
                FROM contacts
                WHERE email ILIKE %s
                ORDER BY first_name;
            """, (f"%{fragment}%",))
            rows = cur.fetchall()
        if not rows:
            print("No contacts found with that email fragment.")
            return
        print(f"{'ID':<5}{'First name':<15}{'Last name':<15}{'Email':<30}")
        for id_, fn, ln, email in rows:
            print(f"{id_:<5}{fn:<15}{(ln or ''):<15}{(email or ''):<30}")
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


def sorted_contacts():
    print("Sort by: 1) name  2) birthday  3) date added")
    choice = input("Choose 1-3: ").strip()
    order_by = {
        "1": "c.first_name, c.last_name",
        "2": "c.birthday NULLS LAST",
        "3": "c.created_at",
    }.get(choice)
    if not order_by:
        print("Invalid choice.")
        return

    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(f"""
                SELECT c.id, c.first_name, c.last_name, c.phone, c.birthday, c.created_at
                FROM contacts c
                ORDER BY {order_by};
            """)
            rows = cur.fetchall()
        if not rows:
            print("No contacts found.")
            return
        print(f"{'ID':<5}{'First name':<15}{'Last name':<15}{'Phone':<18}{'Birthday':<12}{'Added':<20}")
        for id_, fn, ln, phone, bday, created in rows:
            print(f"{id_:<5}{fn:<15}{(ln or ''):<15}{phone:<18}{str(bday or ''):<12}{str(created):<20}")
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


def paginated_navigation():
    """Console loop over Practice 8's get_contacts_paginated() function."""
    try:
        page_size = int(input("Page size (default 5): ").strip() or "5")
    except ValueError:
        print("Must be a number.")
        return

    offset = 0
    while True:
        try:
            rows = _fetch_page(page_size, offset)
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            return

        print(f"\n-- Page starting at offset {offset} --")
        if not rows:
            print("(no more records)")
        else:
            print(f"{'ID':<5}{'First name':<15}{'Last name':<15}{'Phone':<20}")
            for id_, fn, ln, phone in rows:
                print(f"{id_:<5}{fn:<15}{(ln or ''):<15}{phone:<20}")

        cmd = input("[n]ext / [p]rev / [q]uit: ").strip().lower()
        if cmd == "n":
            offset += page_size
        elif cmd == "p":
            offset = max(0, offset - page_size)
        elif cmd == "q":
            break
        else:
            print("Unknown command.")


# ============================================================
# TSIS1 3.3 — Import / Export
# ============================================================

def _get_or_create_group(cur, group_name):
    if not group_name:
        return None
    cur.execute("SELECT id FROM groups WHERE name = %s;", (group_name,))
    row = cur.fetchone()
    if row:
        return row[0]
    cur.execute("INSERT INTO groups (name) VALUES (%s) RETURNING id;", (group_name,))
    return cur.fetchone()[0]


def export_to_json(filepath: str):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT c.id, c.first_name, c.last_name, c.phone, c.email, c.birthday, g.name
                FROM contacts c
                LEFT JOIN groups g ON g.id = c.group_id
                ORDER BY c.id;
            """)
            contacts = cur.fetchall()

            data = []
            for id_, fn, ln, phone, email, bday, group in contacts:
                cur.execute("SELECT phone, type FROM phones WHERE contact_id = %s;", (id_,))
                phones = [{"phone": p, "type": t} for p, t in cur.fetchall()]
                data.append({
                    "first_name": fn,
                    "last_name": ln,
                    "phone": phone,
                    "email": email,
                    "birthday": bday.isoformat() if bday else None,
                    "group": group,
                    "phones": phones,
                })

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=str)
        print(f"Exported {len(data)} contact(s) to {filepath}.")
    except psycopg2.Error as e:
        print(f"Database error during export: {e}")
    except OSError as e:
        print(f"File error during export: {e}")
    finally:
        conn.close()


def import_from_json(filepath: str):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return

    conn = get_connection()
    imported, skipped, updated = 0, 0, 0
    try:
        with conn:
            with conn.cursor() as cur:
                for item in data:
                    fn = item.get("first_name")
                    ln = item.get("last_name")
                    phone = item.get("phone")
                    email = item.get("email")
                    birthday = item.get("birthday")
                    group_name = item.get("group")
                    phones = item.get("phones", [])

                    if not fn or not phone:
                        print(f"Skipping invalid record (missing first_name/phone): {item}")
                        continue

                    cur.execute(
                        "SELECT id FROM contacts WHERE first_name = %s AND COALESCE(last_name, '') = COALESCE(%s, '');",
                        (fn, ln),
                    )
                    existing = cur.fetchone()

                    group_id = _get_or_create_group(cur, group_name)

                    if existing:
                        answer = input(f"Contact '{fn} {ln or ''}' already exists. (s)kip or (o)verwrite? ").strip().lower()
                        if answer != "o":
                            skipped += 1
                            continue
                        contact_id = existing[0]
                        cur.execute(
                            """UPDATE contacts
                               SET last_name = %s, phone = %s, email = %s, birthday = %s, group_id = %s
                               WHERE id = %s;""",
                            (ln, phone, email, birthday, group_id, contact_id),
                        )
                        cur.execute("DELETE FROM phones WHERE contact_id = %s;", (contact_id,))
                        updated += 1
                    else:
                        cur.execute(
                            """INSERT INTO contacts (first_name, last_name, phone, email, birthday, group_id)
                               VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;""",
                            (fn, ln, phone, email, birthday, group_id),
                        )
                        contact_id = cur.fetchone()[0]
                        imported += 1

                    for p in phones:
                        cur.execute(
                            "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s);",
                            (contact_id, p.get("phone"), p.get("type")),
                        )

        print(f"Import finished. New: {imported}, updated: {updated}, skipped: {skipped}.")
    except psycopg2.Error as e:
        print(f"Database error during JSON import: {e}")
    finally:
        conn.close()


def insert_from_csv_extended(filepath: str):
    """Extended CSV import: first_name,last_name,email,birthday,group,phone,phone_type"""
    conn = get_connection()
    inserted = 0
    try:
        with open(filepath, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            with conn:
                with conn.cursor() as cur:
                    for row in reader:
                        fn = (row.get("first_name") or "").strip()
                        ln = (row.get("last_name") or "").strip() or None
                        email = (row.get("email") or "").strip() or None
                        birthday = (row.get("birthday") or "").strip() or None
                        group_name = (row.get("group") or "").strip() or None
                        phone = (row.get("phone") or "").strip()
                        phone_type = (row.get("phone_type") or "mobile").strip()

                        if not fn or not phone:
                            print(f"Skipping row (missing first_name/phone): {row}")
                            continue

                        group_id = _get_or_create_group(cur, group_name)

                        cur.execute(
                            """
                            INSERT INTO contacts (first_name, last_name, phone, email, birthday, group_id)
                            VALUES (%s, %s, %s, %s, %s, %s)
                            ON CONFLICT (phone) DO UPDATE
                                SET first_name = EXCLUDED.first_name,
                                    last_name  = EXCLUDED.last_name,
                                    email      = EXCLUDED.email,
                                    birthday   = EXCLUDED.birthday,
                                    group_id   = EXCLUDED.group_id
                            RETURNING id;
                            """,
                            (fn, ln, phone, email, birthday, group_id),
                        )
                        contact_id = cur.fetchone()[0]

                        if phone_type not in ("home", "work", "mobile"):
                            phone_type = "mobile"
                        cur.execute(
                            "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s);",
                            (contact_id, phone, phone_type),
                        )
                        inserted += 1
        print(f"Imported/updated {inserted} row(s) from {filepath}.")
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except psycopg2.Error as e:
        print(f"Database error during extended CSV import: {e}")
    finally:
        conn.close()


# ============================================================
# TSIS1 3.4 — New stored procedures / function wrappers
# ============================================================

def add_phone_proc():
    name = input("Contact name (first name, or 'First Last'): ").strip()
    phone = input("New phone number: ").strip()
    ptype = input("Type (home/work/mobile): ").strip().lower()
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("CALL add_phone(%s, %s, %s);", (name, phone, ptype))
        for notice in conn.notices:
            print(notice.strip())
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


def move_to_group_proc():
    name = input("Contact name (first name, or 'First Last'): ").strip()
    group_name = input("Target group name: ").strip()
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("CALL move_to_group(%s, %s);", (name, group_name))
        for notice in conn.notices:
            print(notice.strip())
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


def search_contacts_func():
    query = input("Search (matches name / email / any phone): ").strip()
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_contacts(%s);", (query,))
            rows = cur.fetchall()
        if not rows:
            print("Nothing found.")
            return
        by_contact = {}
        for id_, fn, ln, email, group, phone, ptype in rows:
            entry = by_contact.setdefault(id_, {"fn": fn, "ln": ln, "email": email, "group": group, "phones": []})
            if phone:
                entry["phones"].append(f"{phone} ({ptype})")
        for id_, info in by_contact.items():
            print(f"\nID: {id_}  {info['fn']} {info['ln'] or ''}")
            print(f"  Email: {info['email'] or '-'}")
            print(f"  Group: {info['group'] or '-'}")
            print(f"  Phones: {', '.join(info['phones']) if info['phones'] else '-'}")
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


# ============================================================
# Menu / main loop
# ============================================================

MENU = """
==== PhoneBook (TSIS1) ====
--- Practice 7/8 (unchanged) ---
1.  Import contacts from CSV
2.  Add contact from console
3.  Search contacts
4.  Update contact
5.  Delete contact
6.  Show all contacts
7.  Search by pattern (function)
8.  Show page (pagination function)
9.  Upsert contact (procedure)
10. Insert many contacts (procedure, with validation)
11. Delete contact by name/phone (procedure)
--- TSIS1: extended model, search/filter (3.2) ---
12. Show full contacts (email/birthday/group/phones)
13. Filter contacts by group
14. Search contacts by email
15. Sort contacts (name / birthday / date added)
16. Paginated navigation (next/prev/quit)
--- TSIS1: import/export (3.3) ---
17. Export contacts to JSON
18. Import contacts from JSON
19. Import contacts from extended CSV
--- TSIS1: new procedures/function (3.4) ---
20. Add phone to contact (procedure)
21. Move contact to another group (procedure)
22. Search contacts by name/email/phone (function)
0.  Exit
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
        elif choice == "6":
            show_contacts()
        elif choice == "7":
            search_by_pattern_func()
        elif choice == "8":
            show_page_func()
        elif choice == "9":
            upsert_contact_proc()
        elif choice == "10":
            insert_many_proc()
        elif choice == "11":
            delete_contact_proc()
        elif choice == "12":
            show_full_contacts()
        elif choice == "13":
            filter_by_group()
        elif choice == "14":
            search_by_email()
        elif choice == "15":
            sorted_contacts()
        elif choice == "16":
            paginated_navigation()
        elif choice == "17":
            path = input("Output JSON path (default contacts_export.json): ").strip() or "contacts_export.json"
            export_to_json(path)
        elif choice == "18":
            path = input("Input JSON path (default contacts_export.json): ").strip() or "contacts_export.json"
            import_from_json(path)
        elif choice == "19":
            path = input("Extended CSV path (default contacts_extended.csv): ").strip() or "contacts_extended.csv"
            insert_from_csv_extended(path)
        elif choice == "20":
            add_phone_proc()
        elif choice == "21":
            move_to_group_proc()
        elif choice == "22":
            search_contacts_func()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
