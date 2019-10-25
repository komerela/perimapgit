from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
	phone_number = models.CharField(
		max_length= 12,
	)
	guard_for=models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete = models.SET_NULL)

