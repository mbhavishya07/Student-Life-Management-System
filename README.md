# Student Life Management System

A Python CLI application designed to help students track and manage their profile, academic tasks, attendance, subject marks, and daily expenses, with progress summaries.

---

## Features

- **Student Profile Management**: Store and update student name, registration number, and branch[span_0](start_span)[span_0](end_span).
- **Academic Task Tracker**: Add tasks, view pending/completed tasks, and update completion status[span_1](start_span)[span_1](end_span).
- **Attendance Tracker**: Log attended vs. total classes, calculate percentage, and check if attendance meets the 75% threshold[span_2](start_span)[span_2](end_span).
- **Marks Tracker**: Record subject marks, view recorded marks, and compute average performance[span_3](start_span)[span_3](end_span).
- **Expense Manager**: Track daily expenses by category and calculate total expenditure[span_4](start_span)[span_4](end_span).
- **Comprehensive Reports**: Display a complete summary report across academics, attendance, and finances[span_5](start_span)[span_5](end_span).
- **Persistent Data Storage**: Saves all user data automatically to a `student_data.json` file[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span).

---

## File Structure

```text
├── main.py              # Application entry point and menu handler
├── student.py           # Student profile management module
├── academics.py         # Academic tasks tracking module
├── attendance.py        # Attendance management module
├── marks.py             # Marks calculation and management module
├── expenses.py          # Daily expense manager module
├── reports.py           # Overall student summary report module
├── storage.py           # Data persistence and JSON file I/O operations
├── utils.py             # Formatting and UI utility functions
└── student_data.json    # Auto-generated JSON file storing student data