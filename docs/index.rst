.. django-notifyme documentation master file, created by
   sphinx-quickstart on Mon Jul 11 08:48:22 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-notifyme's documentation!
===========================================

A framework for django projects and re-usable apps that aims to provide a clean and flexible
notification solution. Developers can emit user-centric notifications to their users without
knowing the details of how the notification will be delivered by the delivery backends.

Delivery backends could emit notices as:

* on site messages
* emails
* twitter messages
* notifio messages
* jabber
* whatever you can dream of

django-notifyme is *NOT* a replacement for request-by-request messages like
``django.contrib.messages`` provides.



Contents:

.. toctree::
   :maxdepth: 2

   quickstart
   official_delivery_backends
   notification_types
   delivery_backends


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

