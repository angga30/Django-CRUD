from django.conf.urls import include, url
from bsct.urls import URLGenerator
from . import models, views

item_patterns = URLGenerator(
    models.Item).get_urlpatterns(paginate_by=10)
sub_item_patterns = URLGenerator(
    models.SubItem).get_urlpatterns(paginate_by=10)


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/?$', views.search, name='search'),
    url('', include(item_patterns)),
    url('', include(sub_item_patterns)),

]
