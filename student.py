from storage import save_data
from utils import print_heading, pause


def student_profile(data):
    print_heading("STUDENT PROFILE")

    name = input("Enter your name: ")
    reg_no = input("Enter your registration number: ")
    branch = input("Enter your branch: ")

    data["name"] = name
    data["reg_no"] = reg_no
    data["branch"] = branch

    save_data(data)

    print("\nStudent profile saved successfully!")

    pause()