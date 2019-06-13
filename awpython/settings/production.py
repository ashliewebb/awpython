from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

try:
    from .local import *
except ImportError:
    pass
