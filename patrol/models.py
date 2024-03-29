from django.db import models
from django.conf import settings

# Create your models here.

class Patrol(models.Model):

	"""
	Description: Patrol model with time
	"""

	perimeter = models.ForeignKey('perimeters.Perimeter', null=True, blank=True, on_delete = models.CASCADE,related_name='patrols')
	time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	created_by=models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete = models.CASCADE,related_name='user_patrols')

	class Meta:
		pass

		