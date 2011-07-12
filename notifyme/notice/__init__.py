#-*- coding: utf-8 -*-

class NoticeTypeRegistry(dict):
    def register(self, notice_type):
        self[notice_type.identifier] = notice_type

types = NoticeTypeRegistry()
