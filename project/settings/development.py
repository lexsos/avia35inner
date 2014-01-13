import os

from .common import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'sqlite3.db'),
    }
}

INTERNAL_IPS = ('127.0.0.1',)
ALLOWED_HOSTS = INTERNAL_IPS

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = '_6_8%3_#i+di=a5z0gdh_eke%u^oa=f=#ik@px^h&9yp1xqur1'
