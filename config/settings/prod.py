from .base import *
import os

# Production-specific settings
DEBUG = False
ALLOWED_HOSTS = ['your-recipe-app-39c4b4413551.herokuapp.com']

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'replace-this-with-production-secret-key')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'recipe_project'),
        'USER': os.getenv('POSTGRES_USER', 'user'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'password'),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}

# Middleware for static file serving in production
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# WhiteNoise settings (optional, for optimized static file serving)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

