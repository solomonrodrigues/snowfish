# Snowfish Site
## Apps
#### layout
- Basic layout: some common static files and a basic-template (other templates extend this one, main purpose is to include a common html head).
Also contains the home-page and some other simple pages.
#### config
- Contains the project seetings / configuration, and the main urls.py (also wsgi and asgi).
#### snowfishapp
- The actual app I want to create.
## Requirements
Django 4.2.2\
python 3.11.3\
psycopg2

## Dockerization
https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application \
https://blog.logrocket.com/dockerizing-django-app/#prerequisites-for-using-docker \
```
docker build . -t snowfish
docker run snowfish
```

## Resources
https://www.w3schools.com/bootstrap/bootstrap_theme_band.asp
