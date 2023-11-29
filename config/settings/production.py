from .base import *

# import sentry_sdk
import environ
# from sentry_sdk.integrations.django import DjangoIntegration

# env = environ.Env()
# environ.Env.read_env(os.path.join(SETTINGS_DIR, '.env_staging'))

ADMINS = [
  #  ("Snowfish Admins", "snowfishband@gmail.com.au"),
]

SECRET_KEY = "s1et6#@d_^ebw9aq83t2@kpmox9s6c=#%6(ywx-k9+6ex6=##h"

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DATABASE', 'snowfishdb'),
        'USER': os.environ.get('POSTGRES_USER', ''),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
        'HOST': os.environ.get('POSTGRES_HOST', ''),
        'PORT': os.environ.get('POSTGRES_PORT', ''),
    }
}

# CACHES = {
#     'default': {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/2",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }

ALLOWED_HOSTS = [
    '.snowfish.com.au',
    '.vercel.app'
]

CSRF_TRUSTED_ORIGINS = ['https://snowfish.com.au']

# Lockdown settings
INSTALLED_APPS += [
    'lockdown',
]

MIDDLEWARE += [
    'lockdown.middleware.LockdownMiddleware',
]

LOCKDOWN_ENABLED = True
LOCKDOWN_PASSWORDS = ('2023novapumpkin2023',)
LOCKDOWN_AUTHFORM_STAFF_ONLY = False
LOCKDOWN_URL_EXCEPTIONS = [
    r'^/static/*',   # unlock /static/*
    r'^/robots.txt$',
]

# Sentry initialization.
# sentry_sdk.init(
#     dsn="https://3dad7bc2764e4d33a268191bb366853e@o140791.ingest.sentry.io/4505559065821184",
#     environment="staging",
#     integrations=[DjangoIntegration()]
# )

SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

# Prod Security Settings

# If set to a non-zero integer value, the SecurityMiddleware sets the HTTP Strict Transport Security header on all
# responses that do not already have it.
SECURE_HSTS_SECONDS = 60  # Set this to something higher later e.g. 2592000 if everything works in prod

# If True, the SecurityMiddleware redirects all non-HTTPS requests to HTTPS (except for those URLs matching a regular
# expression listed in SECURE_REDIRECT_EXEMPT).
SECURE_SSL_REDIRECT = True

# Whether to use a secure cookie for the session cookie. If this is set to True, the cookie will be marked as “secure”,
# which means browsers may ensure that the cookie is only sent under an HTTPS connection.
SESSION_COOKIE_SECURE = True

# Whether to use a secure cookie for the CSRF cookie. If this is set to True, the cookie will be marked as “secure”,
# which means browsers may ensure that the cookie is only sent with an HTTPS connection.
CSRF_COOKIE_SECURE = True

# If True, the SecurityMiddleware adds the includeSubDomains directive to the HTTP Strict Transport Security header.
# It has no effect unless SECURE_HSTS_SECONDS is set to a non-zero value.
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# If True, the SecurityMiddleware adds the preload directive to the HTTP Strict Transport Security header.
# It has no effect unless SECURE_HSTS_SECONDS is set to a non-zero value.
SECURE_HSTS_PRELOAD = True
