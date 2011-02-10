from settings import *
import logging

DEBUG = False

ADMINS = (
    ('Eric Liu', 'ericzliu@gmail.com '),
)

DATABASES = {
    'default':{
        'ENGINE': 'postgresql_psycopg2',
        'NAME': 'squareone',
        'HOST': 'localhost',
        'USER': 'squareone',
        'PASSWORD': '',
    }
}

SOUTH_DATABASE_ADAPTERS = {
    'default': 'south.db.postgresql_psycopg2',
}

from django.contrib.messages import constants as message_constants
MESSAGE_LEVEL = message_constants.INFO

EMAIL_HOST = 'localhost'
EMAIL_PORT = '1025'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
