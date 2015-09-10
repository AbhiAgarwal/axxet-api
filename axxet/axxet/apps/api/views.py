from django.http import HttpResponseForbidden

from rest_framework import routers, viewsets, status
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_bulk import BulkCreateModelMixin, BulkUpdateModelMixin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import AssetSerializer
from .models import Asset

class BulkListMixin(object):
  """ A mixin to perform bulk operations over HTTP GET. """
  def get_queryset(self):
    """
    An override of the `get_queryset()` method to add the ability to
    retrieve a given set of objects, instead of all the objects in the
    default queryset.
    The client needs to send the request as:
        GET /<resource>/?ids[]=<id1>&ids[]=<id2>,...,ids[]=<idN>
    """
    queryset = super(BulkListMixin, self).get_queryset()
    if self.request.method == 'GET':
      filtering_ids = self.request.query_params.getlist('ids[]')
      if not filtering_ids:
        filtering_ids = self.request.query_params.getlist('ids')
      if filtering_ids:
        if len(filtering_ids) == 1:
          filtering_ids = filtering_ids[0].split(',')
        queryset = queryset.filter(pk__in=filtering_ids)
    return queryset

class BulkListCreateUpdateMixin(BulkCreateModelMixin, BulkUpdateModelMixin, BulkListMixin):
  pass

class BulkListCreateUpdateReadOnlyModelViewSet(
  BulkListCreateUpdateMixin,
  ListCreateAPIView,
  viewsets.ReadOnlyModelViewSet,
):
  """
  A ViewSet extending the default functionality of ReadOnlyModelViewSet with bulk requests
  """
  pass

# ViewSets define the view behavior.
class AssetViewSet(BulkListCreateUpdateReadOnlyModelViewSet):
  queryset = Asset.objects.all()
  serializer_class = AssetSerializer
  model = Asset

  # def list(self, request, pk=None):
  #   if not request.user.is_anonymous():
  #     queryset = Asset.objects.all()
  #     return Response(AssetSerializer(queryset).data)
  #   else:
  #     response = {"detail": "Authentication credentials were not provided."}
  #     return Response(response, status=status.HTTP_403_FORBIDDEN)
