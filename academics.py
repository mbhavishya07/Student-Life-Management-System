from storage import save_data
from utils import print_heading, pause


def academic_tasks(data):

    while True:

        print_heading("ACADEMIC TASKS")

        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            task = input("Enter task: ")

            data["tasks"].append({
                "task": task,
                "completed": False
            })

            save_data(data)

            print("\nTask added successfully!")
            pause()

        elif choice == "2":

            print_heading("YOUR TASKS")

            if len(data["tasks"]) == 0:
                print("No tasks available.")

            else:

                for i, task in enumerate(data["tasks"], start=1):

                    if task["completed"]:
                        status = "Completed"
                    else:
                        status = "Pending"

                    print(f"{i}. {task['task']} - {status}")

            pause()

        elif choice == "3":

            if len(data["tasks"]) == 0:
                print("No tasks available.")
                pause()
                continue

            print_heading("SELECT TASK")

            for i, task in enumerate(data["tasks"], start=1):
                print(f"{i}. {task['task']}")

            try:

                number = int(input("\nEnter task number: "))

                if 1 <= number <= len(data["tasks"]):

                    data["tasks"][number - 1]["completed"] = True

                    save_data(data)

                    print("\nTask completed!")

                else:
                    print("\nInvalid task number.")

            except ValueError:
                print("\nPlease enter a number.")

            pause()

        elif choice == "4":

            break

        else:

            print("\nInvalid choice.")
            pause()