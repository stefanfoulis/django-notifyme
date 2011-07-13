Quickstart
==========

This quickstart guide assumes using the official ``django-notifyme-by-email`` and ``django-notifyme-onsite``
delivery backends are used.

Install the packages::

    pip install django-notifyme
    pip install django-notifyme-by-email
    pip install django-notifyme-onsite

Now add ``notifyme``, ``notifyme_by_email`` and ``notifyme_onsite`` to ``INSTALLED_APPS``.

The delivery backends must be registered somewhere on project startup. It is recommended to place this in ``models.py``
of one of the projects apps. E.g the projects `core` app.::

    import notifyme.delivery
    from notifyme_by_email.delivery import EmailBackend
    notifyme.delivery.backends.register(EmailBackend)

    from notifyme_onsite.delivery import OnsiteStickyBackend
    notifyme.delivery.backends.register(OnsiteStickyBackend)

The ``notifyme_onsite`` delivery backends has some tables and urls of its own, so you'll need to run ``syncdb`` and add
something like ``url(r'^notifyme/', include('notifyme_onsite.urls'))`` to your url patterns.


Notice types need to be registered as well. These are the app specific Notifications that can be emitted. In this
example we will use the bundled ``PrinterOnFireNotification``. This code should also be placed inside a ``models.py``::


    import notifyme.notice
    from notifyme.notice.printer_on_fire import PrinterOnFireNotification
    notifyme.notice.types.register(PrinterOnFireNotification)


See :ref:`notification_types` for information on how to create your own.

Now notices can be emitted using the following api::

    import notifyme.api
    notifyme.api.send([user1, user2, AnonymousUser()], 'printer_on_fire',
                      context={'printer': 'my printer name', 'flames': 'deadly'},
                      is_sticky=True, expires_at=datetime.datetime.now()+datetime.timedelta(minutes=5))

``django-notifyme`` will now try to deliver this notice over all the registered delivery backends. Each backend may have
a different set of features. E.g the Email backend can't send messages to anonymous users, so it will ignore it.
The ``is_sticky`` and ``expires_at`` options exist as a convention and are not mandatory.

* ``is_sticky=True``: this notice should be acknowledge by the user.
* ``expires_at``: the date and time at which this message is no longer useful. Depending on the backend the notice may
  be hidden or removed after that that.


