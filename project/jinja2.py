from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse

from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'debug': settings.DEBUG,
        'SCRIPT_JS_PREFIX': settings.SCRIPT_JS_PREFIX
    })
    return env
