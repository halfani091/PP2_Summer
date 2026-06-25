
import json
import os


print("=== 1. JSON Syntax ===")

json_string = """{
    "name": "Alice",
    "age": 25,
    "is_student": true,
    "grades": [95, 87, 92],
    "address": {
        "city": "Almaty",
        "country": "Kazakhstan"
    },
    "phone": null
}"""

print(json_string)


print("\n=== 2. Parsing JSON (json.loads) ===")

data = json.loads(json_string)

print(f"Type after loads(): {type(data)}")
print(f"Name    : {data['name']}")
print(f"Age     : {data['age']}")
print(f"Student : {data['is_student']}")
print(f"Grades  : {data['grades']}")
print(f"City    : {data['address']['city']}")
print(f"Phone   : {data['phone']}")          # None
print(f"Best grade: {max(data['grades'])}")


print("\n=== 3. Python → JSON (json.dumps) ===")

person = {
    "id": 1,
    "name": "Bob",
    "skills": ["Python", "SQL", "Git"],
    "active": True,
    "salary": None
}


compact = json.dumps(person)
print("Compact :", compact)

pretty = json.dumps(person, indent=4, sort_keys=True, ensure_ascii=False)
print("Pretty:\n", pretty)

# Python → JSON type mapping
print("\nType mapping:")
print(f"  True  → {json.dumps(True)}")    # true
print(f"  False → {json.dumps(False)}")   # false
print(f"  None  → {json.dumps(None)}")    # null


FILENAME = "sample-data.json"

print(f"\n=== 4. Writing JSON to '{FILENAME}' ===")

students = [
    {"id": 1, "name": "Alice",   "gpa": 3.9, "courses": ["Math", "CS"],      "graduated": False},
    {"id": 2, "name": "Bob",     "gpa": 3.5, "courses": ["Physics", "CS"],   "graduated": False},
    {"id": 3, "name": "Charlie", "gpa": 3.7, "courses": ["Math", "Biology"], "graduated": True},
    {"id": 4, "name": "Diana",   "gpa": 4.0, "courses": ["CS", "Chemistry"], "graduated": False},
    {"id": 5, "name": "Eve",     "gpa": 3.2, "courses": ["History", "Math"], "graduated": True},
]

with open(FILENAME, "w", encoding="utf-8") as f:
    json.dump(students, f, indent=4, ensure_ascii=False)

print(f"Saved {len(students)} student records to '{FILENAME}'.")

print(f"\n=== 5. Reading JSON from '{FILENAME}' ===")

with open(FILENAME, "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(f"Loaded {len(loaded)} records:\n")
for s in loaded:
    status  = "graduated" if s["graduated"] else "active"
    courses = ", ".join(s["courses"])
    print(f"  [{s['id']}] {s['name']:<10} GPA={s['gpa']}  {status:<10}  courses: {courses}")


print("\n=== 6. Working with JSON Data ===")


top = [s for s in loaded if s["gpa"] >= 3.7]
print("Top students (GPA ≥ 3.7):")
for s in top:
    print(f"  {s['name']} — {s['gpa']}")

avg = sum(s["gpa"] for s in loaded) / len(loaded)
print(f"\nAverage GPA: {avg:.2f}")

all_courses = sorted({c for s in loaded for c in s["courses"]})
print(f"All courses : {all_courses}")


graduated = sum(1 for s in loaded if s["graduated"])
print(f"Graduated   : {graduated}")
print(f"Active      : {len(loaded) - graduated}")


new_student = {"id": 6, "name": "Frank", "gpa": 3.6, "courses": ["CS", "Physics"], "graduated": False}
loaded.append(new_student)

with open(FILENAME, "w", encoding="utf-8") as f:
    json.dump(loaded, f, indent=4, ensure_ascii=False)

print(f"\nAdded '{new_student['name']}'. File now has {len(loaded)} records.")


print(f"\nFinal content of '{FILENAME}':")
with open(FILENAME, "r", encoding="utf-8") as f:
    print(f.read())


print("=== 7. Error Handling ===")

bad_json = '{"name": "test", "value": }'

try:
    json.loads(bad_json)
except json.JSONDecodeError as e:
    print(f"JSONDecodeError caught: {e}")


os.remove(FILENAME)
print(f"\nCleaned up '{FILENAME}'.")
