===============
django-notifyme
===============

.. warning:: this code is NOT ready for production yet.

A framework for django projects and re-usable apps that aims to provide a clean and flexible
notification solution. Developers can emit user-centric notifications to their users without
knowing the details of how the notification will be delivered by the delivery backends.

Delivery backends could emit notices as:

* emails
* twitter messages
* notifio messages
* jabber
* whatever you can dream of

django-notifyme is *NOT* a replacement for request-by-request messages like
``django.contrib.messages`` provides.
