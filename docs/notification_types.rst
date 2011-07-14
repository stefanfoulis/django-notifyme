.. _notification_types:

notification types
==================

Notification types are app specific. Custom apps define custom NoticeTypes.
In the simplest case, all you need is a ``identifier`` for your custom NoticeType::

    from notifyme.notice.base import BaseNotificationType

    class PrinterOnFireNotification(BaseNotificationType):
        identifier = 'printer_on_fire'

But you can do so much more. Here is a more complete example::

    from notifyme.notice.base import BaseNotificationType
    import datetime

    class PrinterOnFireNotification(BaseNotificationType):
        identifier = 'printer_on_fire'

        def can_send(self, user, backend):
            """
            Never send PrinterOnFireNotifications to 'kristian' after 3 o'clock.
            """
            if user.username == 'kristian' and datetime.datetime.now().time()>datetime.time(15,0):
                return False
            return True

        def get_context(self, language=None):
            """
            perform any context altering actions before the notification is rendered. At this point the active language
            will be set correctly for the user. This is where language specific stuff for the context can be changed.
            This context is shared for all users receiving the notice.
            """
            context = super(PrinterOnFireNotification, self).get_context(language=language)
            if language=='de':
                 context.update({'show_special_link_for_german_only': True})
            return context

        def get_user_context(self, user, language=None):
            """
            Same as 'get_context', but gets called for each individual user that receives the notice.
            """
            context = super(PrinterOnFireNotification, self).get_user_context(language=language)
            if user.username=='kristian':
                context.update({'show_trollface': True})
            return context
