from django.conf import settings
from django.contrib.gis.db import models


# Create your models here.

class CheckPoint(models.Model):
	"""
	Description: Model Description
	"""
	
	perimeter = models.ForeignKey('perimeters.Perimeter', null=True, blank=True, on_delete = models.CASCADE,related_name='perimeter_checkpoints')
	bar_code = models.CharField(null=True, blank=True, max_length=255)
	geo_location = models.PointField(null=True, blank=True, max_length=255)
	floor = models.ForeignKey('floors.Floor',help_text='The perimeter floor is essential to ditinguish points that are geometrically ontop of each other', null=True, blank=True, on_delete = models.CASCADE)

	class Meta:
		pass

	def __str__(self):
		return "{} in {}".format(self.bar_code,self.perimeter.name)

	def serialize(self):
		return {
			'location':self.geo_location,
			'bar_code':self.bar_code
		}