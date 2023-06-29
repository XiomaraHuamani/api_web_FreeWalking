virtualenv vet_backend
.\vet_backend\Scripts\activate
pip install Django

rem django-admin startproject backend
cd backend
rem django-admin startapp ventas

python manage.py runserver 0.0.0.0:9010