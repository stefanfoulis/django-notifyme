#-*- coding: utf-8 -*-

class NotificationTypeRegistry(dict):
    def register(self, notification_type):
        self[notification_type.identifier] = notification_type

registry = NotificationTypeRegistry()
