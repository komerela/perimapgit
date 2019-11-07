from .models import Floor
from django import forms

class FloorCreateForm(forms.ModelForm):
	class Meta():
		model=Floor
		fields=['name','perimeter',]
		widgets = {'perimeter': forms.HiddenInput()}
