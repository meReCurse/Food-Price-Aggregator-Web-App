"""
ASGI config for conf project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from decouple import config


settings_module_name = 'DJANGO_SETTINGS_MODULE'

os.environ.setdefault(settings_module_name, config(settings_module_name))

application = get_asgi_application()
