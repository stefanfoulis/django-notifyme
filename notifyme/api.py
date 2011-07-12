#-*- coding: utf-8 -*-
import notifyme.delivery
import notifyme.notice
import notifyme.tasks
import notifyme.tasks

def send(to_users, notice_type, context=None, **options):
    # get the Notification Class for notice_type
    NoticeClass = notifyme.notice.types.get(notice_type)
    # create an instance of the NoticeClass
    notice = NoticeClass(to_users=to_users, context=context, **options)
    # depending on settings either add the notice to celery or whatever
    #notifyme.tasks.send_notice(notice)
    print notice
    send_now(notice)

def send_now(notice):
    for backend in notifyme.delivery.backends.values():
        print backend, notice
        backend(notice).deliver()