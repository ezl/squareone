DEBUG = True

INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
)

def debug_toolbar_callback(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': debug_toolbar_callback,
}

DATABASES = {
    'default':{
        #'ENGINE': 'postgresql_psycopg2',
        'ENGINE': 'sqlite3',
        'NAME': 'project_DB.sqlite3',
    }
}
SOUTH_DATABASE_ADAPTERS = {
    'default': 'south.db.sqlite3',
}

SOUTH_DATABASE_ADAPTERS = {
    'default': 'south.db.postgresql_psycopg2',
}

EMAIL_HOST = 'localhost'
EMAIL_PORT = '1025'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

NOTIFICATIONS_ENABLED = True
