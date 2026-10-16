# Snowfish Site
## Apps
#### layout
- Basic layout: some common static files and a basic-template (other templates extend this one, main purpose is to include a common html head).
Also contains the home-page and some other simple pages.
#### config
- Contains the project seetings / configuration, and the main urls.py and wsgi.py.
#### snowfishapp
- The actual app I want to create.
## Requirements
Django 4.2.2\
python 3.11.3\
psycopg2

## Local development
```
cp .env.example .env
docker compose up -d          # WEB_PORT=8001 docker compose up -d if 8000 is taken
docker compose exec web python manage.py migrate
```

## Dockerization
https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application \
https://blog.logrocket.com/dockerizing-django-app/#prerequisites-for-using-docker \
```
docker build . -t snowfish
docker run snowfish
```

## Deployment
Vercel deploys `master` to production and other branches to previews, using Vercel's Django framework preset.
- Python version comes from `.python-version`; dependencies from `requirements.txt`.
- Vercel runs `collectstatic` (because `STATIC_ROOT` is set) and serves `/static/` from its CDN.
- `vercel_build.py` runs `migrate` on production builds only. Migrations must be committed; nothing runs `makemigrations` on deploy.
- The database is Neon Postgres in Sydney, read from the `SYD_POSTGRES_*` env vars. Previews use the same live database, so admin edits on a preview change the real site.
- Blog content backup (restore into an empty blog table): `python manage.py loaddata blog_backup`.

## Resources
https://www.w3schools.com/bootstrap/bootstrap_theme_band.asp

## Inspirations
https://www.muse.mu/ \
https://www.midjourney.com/home/?callbackUrl=%2Fapp%2F \
https://github.com/ \
https://www.nbthieves.com/ \
https://docs.djangoproject.com/en/4.2/

## Icon sources
https://blog.hootsuite.com/social-media-icons/

