import os
import dj_database_url


def path(*args):
    return os.path.join(os.path.dirname(__file__), '..', *args)

DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'project'
    }
}
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = ['*']

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = path('public', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = path('public', 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    path('static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '_%a@-1t^jfjh4nnhmsje1785ii36t5h0)ob%4%(r36fa$hihc%'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': (
            path('templates'),
        ),
        'APP_DIRS': False,
        'OPTIONS': {
            'environment': 'project.jinja2.environment'
        }
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': (
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ),
            'loaders': (
                ('django.template.loaders.cached.Loader', (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                )),
            ),
        }
    },
)

INSTALLED_APPS = (
    'flat',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'widget_tweaks',
    'django_extensions',
    'gunicorn',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

SCRIPT_JS_PREFIX = ''
