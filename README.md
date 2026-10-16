<p align="center">
  <a href="https://www.snowfish.com.au">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="layout/static/layout/img/snowfish-logo-white.svg">
      <img src="layout/static/layout/img/snowfish-logo-orange.svg" alt="Snowfish" width="480">
    </picture>
  </a>
</p>

<p align="center">
  The official website of Snowfish, an independent band from Newcastle, Australia.<br>
  <strong><a href="https://www.snowfish.com.au">snowfish.com.au</a></strong>
</p>

---

A Django site the band runs themselves: one place for our music, videos, photos, tour dates, blog and merch. Tour dates, blog posts and the latest-release banner are all edited in the Django admin, so updating the site doesn't need a deploy.

## What's on the site

- **Home**, with the latest release front and centre
- **Music, videos and photos**, with releases linking out to streaming services
- **Tour dates**, each with its own page
- **Blog**, written in the band's own voice
- **Store**, listing merch and how to order it

## Built with

- **Django 5.2 LTS** on Python 3.13
- **Bootstrap 5** with custom CSS
- **PostgreSQL** (Neon, Sydney region)
- **Vercel** for hosting, using its Django framework preset
- **WhiteNoise** for static files and **Sentry** for error tracking

## Project layout

| App | What it holds |
|---|---|
| `config` | Settings (`config/settings/`), root URLs and WSGI entry point |
| `layout` | Base template, shared static files, and the home, about, contact and store pages |
| `snowfishapp` | Music, videos and photos pages, plus the latest-release banner |
| `tour` | Tour dates and their detail pages |
| `blog` | Blog posts, made up of ordered paragraphs |

## Running locally

You'll need Docker.

```bash
cp .env.example .env
docker compose up -d
docker compose exec web python manage.py migrate
```

Then open http://localhost:8000. To restore blog content into an empty blog table, run `docker compose exec web python manage.py loaddata blog_backup`.

## Deployment

Vercel deploys `master` to production and other branches to previews, using its Django framework preset.

- The Python version comes from `.python-version` and dependencies from `requirements.txt`.
- Vercel runs `collectstatic` (because `STATIC_ROOT` is set) and serves `/static/` from its CDN.
- `vercel_build.py` runs `migrate` on production builds only. Migrations must be committed; nothing runs `makemigrations` on deploy.
- The database is read from the `SYD_POSTGRES_*` environment variables. Previews use the same live database, so admin edits on a preview change the real site.
