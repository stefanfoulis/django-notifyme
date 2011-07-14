#-*- coding: utf-8 -*-
from notifyme import notification_types
from celery.task import task

@task
def send_notice(notice):
    from notifyme.api import send_now
    send_now(notice)