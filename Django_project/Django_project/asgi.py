import os

from django.core.asgi import get_asgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_project.settings")
django_asgi_app = get_asgi_application()
