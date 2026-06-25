# ============================================================
# Practice 4 — Python Dates
# ============================================================

from datetime import datetime, date, timedelta

# ----------------------------------------------------------
# Task 1: Subtract five days from current date
# ----------------------------------------------------------
print("=== Task 1: Subtract 5 days from current date ===")
today = date.today()
five_days_ago = today - timedelta(days=5)
print(f"Current date : {today}")
print(f"Five days ago: {five_days_ago}")

# ----------------------------------------------------------
# Task 2: Print yesterday, today, tomorrow
# ----------------------------------------------------------
print("\n=== Task 2: Yesterday, Today, Tomorrow ===")
yesterday = today - timedelta(days=1)
tomorrow  = today + timedelta(days=1)
print(f"Yesterday : {yesterday}")
print(f"Today     : {today}")
print(f"Tomorrow  : {tomorrow}")

# ----------------------------------------------------------
# Task 3: Drop microseconds from datetime
# ----------------------------------------------------------
print("\n=== Task 3: Drop microseconds from datetime ===")
now = datetime.now()
print(f"With microseconds   : {now}")
now_no_microseconds = now.replace(microsecond=0)
print(f"Without microseconds: {now_no_microseconds}")

# ----------------------------------------------------------
# Task 4: Calculate difference between two dates in seconds
# ----------------------------------------------------------
print("\n=== Task 4: Date difference in seconds ===")
date1 = datetime(2024, 1, 1, 0, 0, 0)
date2 = datetime(2024, 12, 31, 23, 59, 59)

diff = date2 - date1
diff_in_seconds = int(diff.total_seconds())
print(f"Date 1      : {date1}")
print(f"Date 2      : {date2}")
print(f"Difference  : {diff_in_seconds} seconds")
