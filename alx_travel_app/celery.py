# alx_travel_app_0x03/alx_travel_app/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

app = Celery('alx_travel_app')

# Load settings from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks from installed apps
app.autodiscover_tasks()

