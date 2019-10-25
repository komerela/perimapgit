from rest_framework import serializers
from .models import PatrolPoint

class PatrolPointSerializer(serializers.ModelSerializer):
	class Meta:
		model = PatrolPoint
		#fields in the model
		fields = ['patrol','id','checkpoint']