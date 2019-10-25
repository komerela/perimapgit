from rest_framework import serializers
from .models import Perimeter


class PerimeterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Perimeter
		#fields in the model
		fields = ['name','id']