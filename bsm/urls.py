from bsm_samples.urls import urlpatterns as bsm_samples_urls

from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

# append urls from bsm_samples app
urlpatterns += bsm_samples_urls
