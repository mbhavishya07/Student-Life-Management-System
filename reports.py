from utils import print_heading, pause


def student_report(data):

    print_heading("STUDENT REPORT")

    print(f"Name        : {data['name']}")
    print(f"Register No : {data['reg_no']}")
    print(f"Branch      : {data['branch']}")

    print("\n---------- ACADEMIC SUMMARY ----------")

    total_tasks = len(data["tasks"])

    completed_tasks = 0

    for task in data["tasks"]:

        if task["completed"]:
            completed_tasks += 1

    print(f"Total Tasks     : {total_tasks}")
    print(f"Completed Tasks : {completed_tasks}")

    if len(data["marks"]) > 0:

        total_marks = 0

        for mark in data["marks"]:
            total_marks += mark["marks"]

        average = total_marks / len(data["marks"])

        print(f"Average Marks   : {average:.2f}")

    else:

        print("Average Marks   : No marks entered")

    print("\n---------- ATTENDANCE ----------")

    attended = data["attendance"]["attended"]
    total = data["attendance"]["total"]

    if total > 0:

        percentage = (attended / total) * 100

        print(f"Attendance: {percentage:.2f}%")

    else:

        print("Attendance: No data entered")

    print("\n---------- EXPENSE SUMMARY ----------")

    total_expense = 0

    for expense in data["expenses"]:
        total_expense += expense["amount"]

    print(f"Total Expenses: ₹{total_expense:.2f}")

    pause()