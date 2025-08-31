# alx_travel_app_0x03/alx_travel_app/__init__.py
from .celery import app as celery_app

__all__ = ['celery_app']

