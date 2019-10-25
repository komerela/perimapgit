from rest_framework import serializers
from .models import Patrol

class PatrolSerializer(serializers.ModelSerializer):
	class Meta:
		model = Patrol
		#fields in the model
		fields = ['time','id','perimeter']