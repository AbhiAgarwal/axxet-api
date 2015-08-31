from rest_framework import routers
from axxet.apps.api.views import (
  UserViewSet,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'data', DataView)
