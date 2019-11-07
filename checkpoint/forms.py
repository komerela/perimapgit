from django import forms
from .models import CheckPoint
from floors.models import Floor
from django.contrib.gis.geos import Point
from decimal import Decimal
from random import randint




class CheckpointCreateForm(forms.ModelForm):
	latitude =forms.DecimalField(label='Latitude', initial="30",help_text='The globe grid coordinate for latitude')
	longitude = forms.DecimalField(label='Longitude', initial="24",help_text='The globe grid coordinate for longitude')


	class Meta():
		model=CheckPoint
		fields = ['perimeter','floor',]
		widgets = {'perimeter': forms.HiddenInput()}



	def save(self, commit=True):
		#Create a point field here from the latitude and longitude
		m=super(CheckpointCreateForm, self).save(commit=commit)
		m.geo_location = Point(float(self.cleaned_data['latitude']),float(self.cleaned_data['longitude']))
		m.bar_code=str(self.random_with_N_digits(10))
		m.save()
		return m

	def random_with_N_digits(self,n):
		range_start = 10**(n-1)
		range_end = (10**n)-1
		return randint(range_start, range_end)