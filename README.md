# Library Management System

A Library Management System web application built with Python and Django.

## Features
- Admin and Student login panels.
- Add, View, and Issue Books.
- Track issued books to students.

## Technology Stack
- Python
- Django (3.0.5)
- SQLite3 (Default Database)
- HTML/CSS/JavaScript

## Database Entity-Relationship Diagram

```mermaid
erDiagram
    User ||--o| StudentExtra : "1 to 1"
    User {
        int id PK
        string username
        string password
    }
    StudentExtra {
        int id PK
        string enrollment "Logical FK"
        string branch
        int user_id FK
    }
    Book {
        int id PK
        string name
        int isbn "Logical FK"
        string author
        string category
    }
    IssuedBook {
        int id PK
        string enrollment "Logical FK"
        string isbn "Logical FK"
        date issuedate
        date expirydate
    }
    StudentExtra ||--o{ IssuedBook : "issues (via enrollment)"
    Book ||--o{ IssuedBook : "issued as (via isbn)"
```

## Setup Instructions

1. **Clone the repository** (if not already cloned)
   ```bash
   git clone https://github.com/Dpjaiswal/librarymanagement.git
   cd librarymanagement
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Linux/Mac:
   source venv/bin/activate
   ```

3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser (for Admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the local development server**
   ```bash
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000/` in your browser.
