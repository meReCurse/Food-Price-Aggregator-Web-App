from .base import *

# SETTING DEV ENVIRONMENT
# -----------------------------------------------------------------------------
# https://github.com/jazzband/django-debug-toolbar

MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

INSTALLED_APPS += ('debug_toolbar', )


# SET ALLOWED IP
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/ref/settings/#internal-ips

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2', ]

