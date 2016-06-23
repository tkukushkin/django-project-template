import os
from project.settings.base import *  # NOQA

TEST_APP_DIR = os.path.dirname(__file__)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(TEST_APP_DIR, 'test.db')
    }
}

MEDIA_ROOT = os.path.join(TEST_APP_DIR, 'public', 'media')
STATIC_ROOT = os.path.join(TEST_APP_DIR, 'public', 'static')

INSTALLED_APPS += ('tests', )
