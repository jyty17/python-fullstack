from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'frontend.settings')

CELERY_BROKER_URL = 'amqp://localhost'

app = Celery('frontend')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# from celery import Celery
from celery.schedules import crontab

#The decorator is used for recognizing a periodic task
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    #Sending the email every 10 Seconds
    # sender.add_periodic_task(10.0, send_feedback_email_task.s('Ankur','ankur@xyz.com','Hello'), name='add every 10')
    # sender.add_periodic_task(10.0, send_task_logger.s('hel10'), name='add every 10')

    # Sends 
    sender.add_periodic_task(30.0, send_task_logger.s('a30n m30w'), expires=10)
  # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     send_feedback_email_task.s('Ankur','ankur@xyz.com','Hello'),)

#The task to be processed by the worker
@app.task
def send_task_logger(message):
    # logger.info(name)
    print(message)