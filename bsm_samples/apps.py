from __future__ import unicode_literals

from watson import search as watson

from django.apps import AppConfig


class SamplesConfig(AppConfig):
    name = 'bsm_samples'

    def ready(self):
        case_number = self.get_model("CaseNumber")
        diagnosis = self.get_model("Diagnosis")
        project = self.get_model("Project")
        sample = self.get_model("Sample")
        sequencing_center = self.get_model("SequencingCenter")
        watson.register(case_number, store=("pk", "get_class_name"))
        watson.register(diagnosis, store=("pk", "get_class_name"))
        watson.register(project, store=("pk", "get_class_name"))
        watson.register(sample, store=("pk", "get_class_name"))
        watson.register(sequencing_center, store=("pk", "get_class_name"))
