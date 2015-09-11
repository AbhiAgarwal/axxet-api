from django.db import models

class AssetQuerySet(models.query.QuerySet):
  def allowed_for_user(self, user):
    return self.filter(user=user)

class AssetManager(models.Manager):
  use_for_related_fields = True

  def get_query_set(self):
    return AssetQuerySet(self.model)

  def allowed_for_user(self, *args, **kwargs):
    return self.get_query_set().allowed_for_user(*args, **kwargs)