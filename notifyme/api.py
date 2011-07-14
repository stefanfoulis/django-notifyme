#-*- coding: utf-8 -*-
from notifyme import delivery_backends, notification_types

def send(to_users, notification_type, context=None, **options):
    # get the Notification Class for notice_type
    NotificationType = notification_types.registry.get(notification_type)
    # create an instance of the NoticeClass
    notification = NotificationType(to_users=to_users, context=context, **options)
    # depending on settings either add the notification to celery or whatever
    send_now(notification)

def send_now(notice):
    for backend in delivery_backends.registry.values():
        backend(notice).deliver()