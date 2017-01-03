from django_crud.urls import urlpatterns as bsm_samples_urls

from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

# append urls from django_crud app
urlpatterns += bsm_samples_urls
