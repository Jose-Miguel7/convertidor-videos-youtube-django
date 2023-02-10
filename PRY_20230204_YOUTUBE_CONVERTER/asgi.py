"""
ASGI config for PRY_20230204_YOUTUBE_CONVERTER project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "PRY_20230204_YOUTUBE_CONVERTER.settings"
)

application = get_asgi_application()
