from marks import marks_section
from storage import load_data, save_data
from student import student_profile
from academics import academic_tasks
from attendance import attendance_section
from expenses import expense_manager
from reports import student_report


data = load_data()


while True:

    print("\n")
    print("======================================")
    print("      STUDENT LIFE MANAGEMENT SYSTEM")
    print("======================================")

    print("1. Student Profile")
    print("2. Academic Tasks")
    print("3. Attendance")
    print("4.marks")
    print("5. Expense Manager")
    print("6. Student Report")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        student_profile(data)

    elif choice == "2":

        academic_tasks(data)

    elif choice == "3":

        attendance_section(data)

    elif choice == "4":

        marks_section(data)

    elif choice == "5":

        expense_manager(data)

    elif choice == "6":

        student_report(data)

    elif choice == "7":

        save_data(data)

        print("\nThank you for using Student Life Management System!")
        print("Goodbye!")

        break

    else:

        print("\nInvalid choice. Please enter 1 to 7.")