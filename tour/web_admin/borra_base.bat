del .\db.sqlite3
rmdir .\web_admin\__pycache__ /s /q
rmdir .\administrador\__pycache__ /s /q
rmdir .\web_admin\migrations\__pycache__ /s /q
rmdir .\administrador\migrations\__pycache__ /s /q
del .\administrador\migrations\*.py /s

python manage.py makemigrations administrador
python manage.py migrate
rem python manage.py migrate --fake

rem python manage.py createsuperuser  --username Pablo  --email pab.gutierrez@duocuc.cl