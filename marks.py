from storage import save_data
from utils import print_heading, pause


def marks_section(data):

    while True:

        print_heading("MARKS")

        print("1. Add Subject Marks")
        print("2. View Marks")
        print("3. Calculate Average")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            subject = input("Enter subject name: ")

            try:

                marks = float(input("Enter marks: "))

                if marks < 0 or marks > 100:
                    print("\nMarks should be between 0 and 100.")
                    pause()
                    continue

                data["marks"].append({
                    "subject": subject,
                    "marks": marks
                })

                save_data(data)

                print("\nMarks added successfully!")

            except ValueError:

                print("\nPlease enter a valid number.")

            pause()

        elif choice == "2":

            print_heading("YOUR MARKS")

            if len(data.get("marks", [])) == 0:
                print("No marks available.")

            else:

                for item in data["marks"]:

                    print(f"{item['subject']}: {item['marks']}")

            pause()

        elif choice == "3":

            if len(data.get("marks", [])) == 0:

                print("No marks available.")

            else:

                total = 0

                for item in data["marks"]:
                    total += item["marks"]

                average = total / len(data["marks"])

                print(f"\nAverage Marks: {average:.2f}")

            pause()

        elif choice == "4":

            break

        else:

            print("\nInvalid choice.")
            pause()