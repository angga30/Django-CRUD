from __future__ import unicode_literals

from watson import search as watson

from django.apps import AppConfig


class SamplesConfig(AppConfig):
    name = 'bsm_samples'

    def ready(self):
        sample = self.get_model("Sample")
        sequencing_center = self.get_model("SequencingCenter")
        project = self.get_model("Project")
        watson.register(sample, store=("pk", "get_class_name"))
        watson.register(sequencing_center, store=("pk", "get_class_name"))
        watson.register(project, store=("pk", "get_class_name"))
