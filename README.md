# Student Life Management System

## Project Overview

The Student Life Management System is a Python-based Command Line Interface (CLI) application developed to help students manage and organize important aspects of their academic and daily life.

The system allows students to manage their personal profile, track academic tasks, monitor attendance, record subject marks, manage daily expenses, and generate a comprehensive student report.

The application uses JSON-based data storage to save student information and records so that the data remains available even after the program is closed.

---

## Features

### 1. Student Profile Management
- Store student name.
- Store registration number.
- Store branch.
- Update student profile information.

### 2. Academic Task Tracker
- Add academic tasks.
- View pending tasks.
- View completed tasks.
- Update the completion status of tasks.

### 3. Attendance Tracker
- Enter attended classes.
- Enter total classes.
- Calculate attendance percentage.
- Check whether attendance meets the required 75% threshold.

### 4. Marks Tracker
- Record subject marks.
- View recorded marks.
- Calculate average marks.
- Track academic performance.

### 5. Expense Manager
- Record daily expenses.
- Categorize expenses.
- View recorded expenses.
- Calculate total expenditure.

### 6. Comprehensive Student Report
- Display student profile information.
- Display academic tasks.
- Display attendance percentage.
- Display subject marks and average marks.
- Display total expenses.
- Provide a combined summary of student information.

### 7. Persistent Data Storage
- Automatically save data to `student_data.json`.
- Load previously saved data when the application starts.
- Prevent loss of data between program sessions.

---

## Technologies / Tools Used

| Technology / Tool | Purpose |
|---|---|
| Python | Main programming language |
| Visual Studio Code | Development environment |
| JSON | Data storage |
| Git | Version control |
| GitHub | Project repository and submission |

---

## Project Structure

```text
Student-Life-Management-System/
│
├── main.py
├── student_data.json
├── README.md
└── screenshots/
    ├── main_menu.png
    ├── attendance.png
    ├── marks.png
    └── student_report.png