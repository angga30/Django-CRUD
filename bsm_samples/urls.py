from django.conf.urls import include, url
from bsct.urls import URLGenerator
from . import models, views

project_patterns = URLGenerator(models.Project).get_urlpatterns(paginate_by=3)
sample_patterns = URLGenerator(models.Sample).get_urlpatterns(paginate_by=3)
sequencing_center_patterns = URLGenerator(
    models.SequencingCenter).get_urlpatterns(paginate_by=3)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('', include(sample_patterns)),
    url('', include(sequencing_center_patterns)),
    url('', include(project_patterns))
]
