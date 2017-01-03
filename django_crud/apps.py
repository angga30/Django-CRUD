from __future__ import unicode_literals

from watson import search as watson

from django.apps import AppConfig


class SamplesConfig(AppConfig):
    name = 'django_crud'

    def ready(self):
        item = self.get_model("Item")
        sub_item = self.get_model("SubItem")
        watson.register(item, store=("pk", "get_class_name"))
        watson.register(sub_item, store=("pk", "get_class_name"))
