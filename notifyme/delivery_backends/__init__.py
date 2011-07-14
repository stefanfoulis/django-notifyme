#-*- coding: utf-8 -*-

class DeliveryBackendRegistry(dict):
    def register(self, backend):
        self[backend.identifier] = backend

registry = DeliveryBackendRegistry()
