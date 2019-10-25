from django.db import models
from django.conf import settings

# Create your models here.

class Perimeter(models.Model):
    """
    Description: Perimeter model with user & name
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete = models.CASCADE)
    name = models.CharField(null=True, blank=True, max_length=100)
    

    class Meta:
        pass