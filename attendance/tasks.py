from __future__ import absolute_import, unicode_literals
from celery import shared_task

@shared_task
def add(self):
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def printing():
    print("just printing")