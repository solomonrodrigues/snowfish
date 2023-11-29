from .base import *

# import sentry_sdk
import environ
# from sentry_sdk.integrations.django import DjangoIntegration

env = environ.Env()
environ.Env.read_env(os.path.join(SETTINGS_DIR, '.env_staging'))

ADMINS = [
  #  ("Snowfish Admins", "snowfishband@gmail.com.au"),
]

SECRET_KEY = "s1et6#@d_^ebw9aq83t2@kpmox9s6c=#%6(ywx-k9+6ex6=##h"

DEBUG = True
SERVE_MEDIA = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'chargermate',
        'USER': 'postgres',
        'PASSWORD': '',
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

ALLOWED_HOSTS = ['.snowfish.com.au']
CSRF_TRUSTED_ORIGINS = ['https://snowfish.com.au']

# Lockdown settings
INSTALLED_APPS += [
    'lockdown',
]

MIDDLEWARE += [
    'lockdown.middleware.LockdownMiddleware',
]

LOCKDOWN_ENABLED = True
LOCKDOWN_PASSWORDS = ('PowerTime251',)
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
