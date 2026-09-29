from storage import save_data
from utils import print_heading, pause


def expense_manager(data):

    while True:

        print_heading("EXPENSE MANAGER")

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            category = input("Enter expense category: ")

            try:

                amount = float(input("Enter amount: ₹"))

                if amount < 0:
                    print("\nAmount cannot be negative.")
                    pause()
                    continue

                data["expenses"].append({
                    "category": category,
                    "amount": amount
                })

                save_data(data)

                print("\nExpense added successfully!")

            except ValueError:

                print("\nPlease enter a valid amount.")

            pause()

        elif choice == "2":

            print_heading("YOUR EXPENSES")

            if len(data["expenses"]) == 0:

                print("No expenses recorded.")

            else:

                for i, expense in enumerate(data["expenses"], start=1):

                    print(
                        f"{i}. {expense['category']} - "
                        f"₹{expense['amount']:.2f}"
                    )

            pause()

        elif choice == "3":

            total = 0

            for expense in data["expenses"]:
                total += expense["amount"]

            print(f"\nTotal Expenses: ₹{total:.2f}")

            pause()

        elif choice == "4":

            break

        else:

            print("\nInvalid choice.")
            pause()