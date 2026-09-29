import json
import os

DATA_FILE = "student_data.json"


def load_data():

    if os.path.exists(DATA_FILE):

        with open(DATA_FILE, "r") as file:
            data = json.load(file)

    else:

        data = {}

    # Student profile
    if "name" not in data:
        data["name"] = ""

    if "reg_no" not in data:
        data["reg_no"] = ""

    if "branch" not in data:
        data["branch"] = ""

    # Academic tasks
    if "tasks" not in data:
        data["tasks"] = []

    # Marks
    if "marks" not in data:
        data["marks"] = []

    # Attendance
    if "attendance" not in data:
        data["attendance"] = {}

    if "attended" not in data["attendance"]:
        data["attendance"]["attended"] = 0

    if "total" not in data["attendance"]:
        data["attendance"]["total"] = 0

    # Expenses
    if "expenses" not in data:
        data["expenses"] = []

    return data


def save_data(data):

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)