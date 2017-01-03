from __future__ import unicode_literals

from watson import search as watson

from django.apps import AppConfig


class Config(AppConfig):
    name = 'django_crud'

    def ready(self):
        item = self.get_model("Item")
        watson.register(item, store=("pk", "get_class_name"))
