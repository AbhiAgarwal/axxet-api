from django.contrib.auth.models import User

class Organization(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  organization_name = models.CharField(max_length=100)
