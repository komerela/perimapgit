from django.db import models
from django.conf import settings

# Create your models here.

class Floor(models.Model):
    """
    Description: class floor model
    """
    
    name = models.CharField(null=True, blank=True, max_length=255)
    perimeter = models.ForeignKey('perimeters.Perimeter', null=True, blank=True, on_delete = models.CASCADE)

    class Meta:
        pass

    def __str__(self):
    	return "Floor {}".format(self.name)