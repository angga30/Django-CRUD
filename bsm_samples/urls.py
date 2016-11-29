from django.conf.urls import include, url
from bsct.urls import URLGenerator
from . import models, views

case_number_patterns = URLGenerator(
    models.CaseNumber).get_urlpatterns(paginate_by=10)
diagnosis_patterns = URLGenerator(
    models.Diagnosis).get_urlpatterns(paginate_by=10)
project_patterns = URLGenerator(models.Project).get_urlpatterns(paginate_by=10)
sample_patterns = URLGenerator(models.Sample).get_urlpatterns(paginate_by=10)
sequencing_center_patterns = URLGenerator(
    models.SequencingCenter).get_urlpatterns(paginate_by=10)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/?$', views.search, name='search'),
    url('', include(case_number_patterns)),
    url('', include(diagnosis_patterns)),
    url('', include(project_patterns)),
    url('', include(sample_patterns)),
    url('', include(sequencing_center_patterns))
]
