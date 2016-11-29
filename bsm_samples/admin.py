from django.contrib import admin
from .models import Project, Sample, SequencingCenter

admin.site.register(Project)
admin.site.register(Sample)
admin.site.register(SequencingCenter)
