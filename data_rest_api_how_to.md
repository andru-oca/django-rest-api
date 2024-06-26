## Steps to create an model and a rest api with peliculas

- install dependecies : django djangorestframework  djangorestframework-simplejwt  django-cors-headers

```bash
python -m venv venv && source ./venv/bin/activate && pip install -r requirements.txt
```
- start project and apps modules
- create project and two modules : users (to be able to access validate users) & peliculas (be able to make CRUD)

```bash
django-admin startproject peliculas_api .
python manage.py startapp app_pelicula & \
python manage.py startapp app_user
```
- modify /peliculas_api/settings.py

```python
INSTALLED_APPS += [
    ...
    'app_pelicula',
    'app_user',
    'rest_framework', 
]

- modificar el archivo models del app_pelicula
- registrar en admin el modelo app_pelicula



```
- START THE MIGRATION WITH THE DATABASE:

```bash
python manage.py makemigrations
python manage.py migrate
```

- CREATE SUPER USER
```bash
python manage.py createsuperuser
```


- START PROJECT 
```bash
python manage.py runserver 
```


- OBTAIN TOKEN 
```bash
curl -X POST http://localhost:8000/user/token/ -d "username=ander" -d "password=123"
# sample -->
TOKEN_API=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5MzQxMTc4LCJpYXQiOjE3MTkzNDA4NzgsImp0aSI6ImE5ODNlZTk0MjU5OTQ5ZWNiYWQ5ZGNkNjgxZGUxNTk1IiwidXNlcl9pZCI6MX0.Qmxwp1TNjwz_WM892z7UN5USvAyvXHgFHHcSOcGIKlI
```

- GET ALL PELICULA
```bash

TOKEN_API=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5MzQxMTc4LCJpYXQiOjE3MTkzNDA4NzgsImp0aSI6ImE5ODNlZTk0MjU5OTQ5ZWNiYWQ5ZGNkNjgxZGUxNTk1IiwidXNlcl9pZCI6MX0.Qmxwp1TNjwz_WM892z7UN5USvAyvXHgFHHcSOcGIKlI

curl -X POST http://localhost:8000/pelicula/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $TOKEN_API" \
-d '{
    "nombre": "Stach",
    "fecha_de_release": "2024-06-25",
    "genero": "Sci Fi"
}'


curl -X GET http://localhost:8000/pelicula/ \
-H "Authorization: Bearer $TOKEN_API"


```

- USER

```bash
curl -X POST http://localhost:8000/user/api/ \
-H "Content-Type: application/json" \
-d '{
    "username": "miguel",
    "email": "miguel@mail.com",
    "password": "123"
}'
```








