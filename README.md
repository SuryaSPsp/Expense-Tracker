# Expense-Tracker
    A simple Expense Tracker web application built using Django and SQLite.
    This project allows users to manage their daily expenses, categorize them, and view expense records easily.

🚀 Features
      Add new expenses with amount, category, and date
      View all expenses in a list
      Categorize expenses (Food, Travel, Rent, etc.)
      Uses SQLite (default Django database)
      Simple and clean Django project structure
      
🛠️ Tech Stack
      Backend: Django (Python)
      Database: SQLite
      Version Control: Git & GitHub

⚙️ Setup Instructions
      Follow these steps to run the project locally:
        git clone https://github.com/SuryaSPsp/Expense-Tracker.git
        cd Expense-Tracker
        python -m venv venv
        venv\Scripts\activate
        pip install -r requirements.txt
        python manage.py migrate
        python manage.py runserver

    Open browser and visit:
        http://127.0.0.1:8000/
🗄️ Database
      Uses SQLite
      No external database setup required
      Database file: db.sqlite3

📌 Notes
    This is a sample Django project
    Authentication is not included
