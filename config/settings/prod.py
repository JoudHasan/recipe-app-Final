from .base import *
import dj_database_url

# Production-specific settings
DEBUG = False

# Secret key should always come from an environment variable in production
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'fallback-secret-key')

# Allowed hosts should include your production domains
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Database settings using dj_database_url
DATABASES = {
    'default': dj_database_url.config(conn_max_age=500, ssl_require=True)
}

# Security settings for production
SECURE_HSTS_SECONDS = 31536000  # Enforce HTTPS for 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Static and media files in production
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Middleware for static file serving in production
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
