#-*- coding: utf-8 -*-
from django.conf import settings

USE_CELERY = getattr(settings, 'NOTIFYME_USER_CELERY', False)