delivery backends
=================


Delivery backends are responsible for actually delivering a notice to the user in some form. The most important
method on the DeliveryBackend class is ``deliver_to``.::

    from notifyme.delivery.base import BaseDeliveryBackend
    class ConsoleNotification(BaseDeliveryBackend):
        def deliver_to(self, user, context, notice, language):
             """
             context is the context that was provided when sending the notice, already manipulated for the user and
             his language.
             """
             msg = render_to_string(
                (
                    "notifyme/notices/%s/console/msg.txt" % notice.identifier,
                    "notifyme/notices/generic/console/msg.txt",
                ), context_instance=context)
             print msg

The corresponsing template in ``notifyme/notices/printer_on_fire/console/msg.txt`` could be::

    {% load i18n %}{% blocktrans %}notifyme console message for %(user)s{% endblocktrans %}: {% trans 'printer' %}: {{ printer }} {% trans 'flames' %}: {{ flames }}

