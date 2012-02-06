from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

urlpatterns = patterns('geoimage.views',
    url(r'^image$',
        'geoimage',
        name="geoimage"),
    )
