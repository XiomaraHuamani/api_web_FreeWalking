rem pip list 
pip install virtualenv
virtualenv veterinaria
cd veterinaria
Scripts\activate
pip install Django
rem django-admin startproject backend
django-admin startproject frontend
cd frontend
rem python manage.py runserver
python manage.py runserver 0.0.0.0:9000

=============================

django-admin startapp ventas
.- agregar la ventas al settings de nuestro proyecto




Correr V2
virtualenv veterinaria
cd veterinaria
Scripts\activate
pip install Django
cd frontend
python manage.py runserver 0.0.0.0:9000