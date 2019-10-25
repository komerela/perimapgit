from django.conf import settings
from django.contrib.gis.db import models

# Create your models here.

class PatrolPoint(models.Model):
    """
    Description: Model Description
    """
    
    patrol = models.ForeignKey('patrol.Patrol', null=True, blank=True, on_delete = models.CASCADE)
    checkpoint = models.ForeignKey('checkpoint.Checkpoint', null=True, blank=True, on_delete = models.CASCADE)


    class Meta:
        pass