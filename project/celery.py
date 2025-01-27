from celery import Celery
import time
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.prod')

app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task
def add(x, y):
    time.sleep(10)
    return x + y

