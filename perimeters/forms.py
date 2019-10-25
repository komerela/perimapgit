from django.db import models
from django.forms import ModelForm
from .models import Perimeter

class PerimeterForm(ModelForm):
	class Meta:
		model = Perimeter
		fields = ['name',]