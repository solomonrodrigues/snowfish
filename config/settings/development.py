from .base import *

DEBUG = True
SERVE_MEDIA = DEBUG
WSGI_APPLICATION = 'config.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DB_NAME', 'snowfishdb'),
#         'USER': os.environ.get('DB_USER', ''),
#         'PASSWORD': os.environ.get('DB_PASSWORD', ''),
#         'HOST': os.environ.get('DB_HOST', ''),
#         'PORT': os.environ.get('DB_PORT', ''),
#     }
# }

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ['127.0.0.1']
# INSTALLED_APPS += [
#     'debug_toolbar',
# ]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://0.0.0.0:3000',
]

STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
