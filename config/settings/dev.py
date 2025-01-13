from .base import *

# Development-specific settings
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Database settings for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
