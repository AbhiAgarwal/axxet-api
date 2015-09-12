from django.db import models
from django.contrib.auth.models import User

from .managers import AssetManager


class Asset(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(
                             User,
                             related_name='asset_user',
                             verbose_name='Owner'
                            )
    objects = AssetManager()
