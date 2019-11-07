from django.db import models
from django.conf import settings

# Create your models here.

class Floor(models.Model):
    """
    Description: class floor model
    """
    
    name = models.CharField(null=True, blank=True,help_text='Provide a name that can uniquely identify this floor on the perimeter', max_length=255)
    perimeter = models.ForeignKey('perimeters.Perimeter', null=True, blank=True, on_delete = models.CASCADE,related_name='floors')

    class Meta:
        pass

    def __str__(self):
    	return "Floor {}".format(self.name)