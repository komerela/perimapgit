from rest_framework import serializers
from .models import CheckPoint

class CheckPointSerializer(serializers.ModelSerializer):
	class Meta:
		model = CheckPoint
		#fields in the model
		fields = ['perimeter','bar_code','geo_location','floor','id']

	