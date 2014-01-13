from .common import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'avia35',
        'USER': 'avia35',
        'HOST': 'localhost',
        'PORT': '',
        'PASSWORD': '',
    }
}

INSTALLED_APPS += (
    'gunicorn',
)

try:
    from .secret import SECRET_KEY
except:
    print 'Need secret.py file with SECRET_KEY'
