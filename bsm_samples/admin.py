from django.contrib import admin
from .models import CaseNumber, Diagnosis, Project, Sample, SequencingCenter

admin.site.register(CaseNumber)
admin.site.register(Diagnosis)
admin.site.register(Project)
admin.site.register(Sample)
admin.site.register(SequencingCenter)
