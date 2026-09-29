from storage import save_data
from utils import print_heading, pause


def attendance_section(data):

    print_heading("ATTENDANCE")

    try:

        attended = int(input("Enter classes attended: "))
        total = int(input("Enter total classes: "))

        if total <= 0:
            print("\nTotal classes must be greater than zero.")
            pause()
            return

        if attended < 0 or attended > total:
            print("\nInvalid attendance values.")
            pause()
            return

        data["attendance"]["attended"] = attended
        data["attendance"]["total"] = total

        percentage = (attended / total) * 100

        save_data(data)

        print(f"\nAttendance Percentage: {percentage:.2f}%")

        if percentage >= 75:
            print("Status: Attendance requirement currently met.")
        else:
            print("Status: Attendance is below 75%.")

    except ValueError:

        print("\nPlease enter valid numbers.")

    pause()