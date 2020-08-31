import os
from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DJANGO_DB_NAME_PRODUCTION"),
        'USER': env("DJANGO_DB_USERNAME_PRODUCTION"),
        'PASSWORD': env("DJANGO_DB_PASSWORD"),
        'HOST': env("DJANGO_DB_HOST_PRODUCTION"),
        'PORT': env("DJANGO_DB_PORT"),
    }
}