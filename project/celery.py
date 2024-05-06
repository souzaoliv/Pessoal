from celery import Celery
import time
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.dev')

app = Celery('project', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

app.autodiscover_tasks()

@app.task
def add(x, y):
    time.sleep(10)
    return x + y

