# Django CSV Upload API
This project is a Django-based REST API that allows users to upload CSV files containing user data (name, email, and age). The uploaded data is validated, stored in the database, and provides detailed feedback about valid and invalid records.

## Installation Steps
1. Set up a virtual environment: venv\Scripts\activate
2. Install dependencies: pip install -r requirements.txt
3. Run migrations: python manage.py makemigrations  python manage.py migrate
4. Start the development server: python manage.py runserver


## Endpoints:
  POST /api/upload-csv/

## Running Tests:
  python manage.py test
