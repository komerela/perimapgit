from django.db import models
from django.conf import settings
from django.contrib.gis.db import models as gis_models


# Create your models here.

class CheckPoint(gis_models.Model):
    """
    Description: Model Description
    """
    
    perimeter = models.ForeignKey('perimeters.Perimeter', null=True, blank=True, on_delete = models.CASCADE)
    bar_code = models.CharField(null=True, blank=True, max_length=255)
    geo_location = gis_models.PointField(null=True, blank=True, max_length=255)
    floor = models.ForeignKey('floors.Floor', null=True, blank=True, on_delete = models.CASCADE)

    class Meta:
        pass