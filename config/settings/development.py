from .base import *

DEBUG = True
SERVE_MEDIA = DEBUG
WSGI_APPLICATION = 'config.wsgi.app'
ROOT_URLCONF = 'config.urls'

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

# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '[::1]',
    '.vercel.app'
]
INTERNAL_IPS = ['127.0.0.1']
# INSTALLED_APPS += [
#     'debug_toolbar',
# ]

# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:3000',
#     'http://0.0.0.0:3000',
# ]

STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
