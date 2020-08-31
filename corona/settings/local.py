from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DJANGO_DB_NAME"),
        'USER': env("DJANGO_DB_USERNAME"),
        'PASSWORD': env("DJANGO_DB_PASSWORD"),
        'HOST': env("DJANGO_DB_HOST"),
        'PORT': env("DJANGO_DB_PORT"),
    }
}