from django.http import HttpResponseForbidden

from rest_framework import routers, viewsets, status
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_bulk import BulkCreateModelMixin, BulkUpdateModelMixin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from axxet.apps.common.views import BulkListCreateUpdateReadOnlyModelViewSet

from .serializers import AssetSerializer
from .models import Asset

class AssetViewSet(BulkListCreateUpdateReadOnlyModelViewSet):
  queryset = Asset.objects.all()
  serializer_class = AssetSerializer
  model = Asset
  
  def list(self, request):
    queryset = Asset.objects.allowed_for_user(request.user)
    serializer = AssetSerializer(queryset, many=True)
    return Response(serializer.data)

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)