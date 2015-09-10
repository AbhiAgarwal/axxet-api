from rest_framework import routers
from axxet.apps.common.views import (
  UserViewSet,
)
from axxet.apps.api.views import (
  AssetViewSet,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'assets', AssetViewSet)
