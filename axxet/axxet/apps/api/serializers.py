from .models import Asset
from rest_framework import serializers

# Serializers define the API representation.
class AssetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Asset
    fields = ('owner', )
