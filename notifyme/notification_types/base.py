#-*- coding: utf-8 -*-

class BaseNotificationType(object):
    def __init__(self, to_users, context, **options):
        self.to_users = to_users
        self.context = context
        self.options = options

    def can_send(self, user, backend):
        return True

    def get_context(self, language=None):
        context = self.context
        context.update({'options': self.options})
        return context

    def get_user_context(self, user, language=None):
        return {'user': user}