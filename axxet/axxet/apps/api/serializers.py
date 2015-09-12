from rest_framework import serializers
# from rest_framework.relations import PrimaryKeyRelatedField

from .models import Asset


# Serializers define the API representation.
class AssetSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    # user = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Asset
        fields = (
            'id', 'name'
        )
