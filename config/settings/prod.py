#from .base import *
#import dj_database_url

# Production-specific settings
#DEBUG = False

# Secret key should always come from an environment variable in production
#SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'fallback-secret-key')

# Allowed hosts should include your production domains
#ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Database settings using dj_database_url
#DATABASES = {
 #   'default': dj_database_url.config(conn_max_age=500, ssl_require=True)
#}

# Static and media files in production
#STATIC_ROOT = BASE_DIR / 'staticfiles'
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Middleware for static file serving in production
#MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
'