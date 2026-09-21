import json
from datetime import datetime

FILE_NAME = "attendance_log.json"


def load_data():
    """Load student and attendance data from the JSON file."""
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "students": [],
            "attendance": []
        }


def save_data(data):
    """Save data to the JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def create_student():
    """Create and save a new student profile."""
    data = load_data()

    print("\n===== CREATE STUDENT =====")

    name = input("Enter student name: ").strip()
    student_id = input("Enter student ID: ").strip()

    if not name or not student_id:
        print("Name and Student ID are required.")
        return

    # Check whether the Student ID already exists
    for student in data["students"]:
        if student["student_id"] == student_id:
            print("A student with this ID already exists.")
            return

    student = {
        "student_id": student_id,
        "name": name
    }

    data["students"].append(student)

    save_data(data)

    print(f"Student {name} registered successfully.")


def check_in_student():
    """Record a student's Present or Late attendance."""
    data = load_data()

    print("\n===== STUDENT CHECK-IN =====")

    student_id = input("Enter student ID: ").strip()

    # Find the student
    student = None

    for item in data["students"]:
        if item["student_id"] == student_id:
            student = item
            break

    if student is None:
        print("Student not found. Please register the student first.")
        return

    status = input("Enter status (Present/Late): ").strip().capitalize()

    if status not in ["Present", "Late"]:
        print("Invalid status. Please enter Present or Late.")
        return

    now = datetime.now()

    attendance_record = {
        "student_id": student["student_id"],
        "name": student["name"],
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "status": status
    }

    data["attendance"].append(attendance_record)

    save_data(data)

    print(
        f"{student['name']} has been marked "
        f"{status} at {now.strftime('%H:%M:%S')}."
    )


def todays_attendance():
    """Display all students checked in today."""
    data = load_data()

    today = datetime.now().strftime("%Y-%m-%d")

    print("\n===== TODAY'S ATTENDANCE =====")
    print(f"Date: {today}")

    records = []

    for record in data["attendance"]:
        if record["date"] == today:
            records.append(record)

    if not records:
        print("No students have checked in today.")
        return

    for record in records:
        print(
            f"ID: {record['student_id']} | "
            f"Name: {record['name']} | "
            f"Status: {record['status']} | "
            f"Time: {record['time']}"
        )