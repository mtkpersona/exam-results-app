# Exam Results Web App

A simple web app for students to check their exam results and for admins to manage results. Built with **Flask**, **SQLite**, and **Bootstrap**.

---

## Features

- **Student View**: Enter a student ID to view results and grades for 15 subjects.
- **Admin View**: Add, view, and delete exam results.
- **Automated Setup**: Database is created and updated automatically.

---

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/exam-results-app.git
   cd exam-results-app

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the app:
   ```bash
   python run.py

## Usage
- **Student Page**: Open http://localhost:5000
- **Admin PAge**: Open http://localhost:5000/admin

## Project Structure
   ```bash
   exam-results-app/
   ├── app/              # Flask app files
      ├── templates/       # Storing all the webpages
         ├── index.html       # Student page template
         └── admin.html       # Admin page template
      ├── __init__.py      # Flask app initialization
      ├── models.py        # Database models
      └── routes.py        # Flask routes
   ├── migrations/       # Database migrations
   ├── instance/         # Database file location
      └── exam_results.db
   ├── requirements.txt  # Dependencies
   ├── run.py            # Application entry point
   ├── startup.py        # Database initialization script
   └── README.md         # Project documentation