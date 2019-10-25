from rest_framework import serializers
from .models import Floor

class FloorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Floor
		#fields in the model
		fields = ['name','id','perimeter']