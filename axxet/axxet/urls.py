from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponseRedirect

from axxet.apps.router_v1 import router

# Admin
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^devdocs/', include('rest_framework_swagger.urls')),
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns += patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-key/get/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api-key/refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
    url(r'^api-key/verify/', 'rest_framework_jwt.views.verify_jwt_token'),
    url(r'^accounts/', include('allauth.urls')),
)
