from .base import *

import sentry_sdk
import environ
from sentry_sdk.integrations.django import DjangoIntegration

# env = environ.Env()
# environ.Env.read_env(os.path.join(SETTINGS_DIR, '.env_staging'))

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

ALLOWED_HOSTS = [
    '.snowfish.com.au',
    '.vercel.app'
]

CSRF_TRUSTED_ORIGINS = ['https://snowfish.com.au']

# Sentry initialization.
sentry_sdk.init(
    dsn="https://811d34389310d960d39dab8c12a4a73f@o4506320558555136.ingest.sentry.io/4506320560586752",
    environment="prod",
    integrations=[DjangoIntegration()]
)

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

# will be notified of 500 errors by email.
ADMINS = [
    ("Solomon Rodrigues", "solomonrodrigues@hotmail.com")
]

# will be notified of 404 errors. IGNORABLE_404_URLS can help filter out spurious reports.
MANAGERS = [
    ("Solomon Rodrigues", "solomonrodrigues@hotmail.com")
]

IGNORABLE_404_URLS = []

STATIC_URL = '/static/'

# Include the path to the 'static' directory within the 'layout' app
STATICFILES_DIRS = [
    BASE_DIR / 'layout' / 'static',
]

# Specify the directory where 'collectstatic' will gather static files for deployment
STATIC_ROOT = BASE_DIR / 'staticfiles_build' / 'static'

# Whitenoise settings
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

