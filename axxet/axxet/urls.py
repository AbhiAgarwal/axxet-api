from django.conf.urls import patterns, include, url
from django.contrib import admin

from axxet.apps.router_v1 import router

# Admin
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns += patterns('',
  url(r'^api/', include(router.urls)),
  url(r'^api/get-api-key/', 'rest_framework_jwt.views.obtain_jwt_token'),
  url(r'^api/refresh-api-key/', 'rest_framework_jwt.views.refresh_jwt_token'),
  url(r'^api/verify-api-key/', 'rest_framework_jwt.views.verify_jwt_token'),
  url(r'^accounts/', include('allauth.urls')),
)
