#-*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.sites.models import Site
from django.utils.translation import get_language, activate
from django.template.context import Context


def get_language_for_user(user):
    return user.get_profile().preferred_language


class BaseDeliveryBackend(object):
    """
    Base backend for all DeliveryBackends
    """
    supports_anonymous_users = False

    def __init__(self, notification):
        self.notification = notification

    def can_send(self, user, notification):
        """
        Determines if this backend should send a notification for the given combination of user and notice_type
        """
        return True

    def get_site(self):
        return Site.objects.get_current()

    def default_context(self):
        return Context({
            'default_http_protocol': getattr(settings, "DEFAULT_HTTP_PROTOCOL", "http"),
            'site': self.get_site(),
            'notification': self.notification,
        })

    def deliver(self):
        """
        deliver the given Notice to_users.
        """
        current_language = get_language()

        for user in self.notification.to_users:
            if not self.supports_anonymous_users and user.is_anonymous():
                continue
            elif user.is_anonymous():
                languages = [language_code for language_code, language in settings.LANGUAGES]
                user = None
            else:
                languages = [get_language_for_user(user)]
            if not (self.notification.can_send(user, self) and self.can_send(user, self.notification)):
                continue
            for language in languages:
                activate(language)
                # build the context
                context = self.default_context()
                context.update(self.notification.get_context(language=language))
                context.update(self.notification.get_user_context(user))
                self.deliver_to(user=user,
                                context=context,
                                notification=self.notification,
                                language=language)
        activate(current_language)


    def deliver_to(self, user, context, notification, language):
        """
        handle delivery to a specific user. In this method the correct language of the user is already set and
        the context has been modified accordingly for this user.
        """
        raise NotImplementedError()