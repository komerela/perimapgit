from rest_framework import viewsets
from .serializers import PatrolPointSerializer
from .models import PatrolPoint

class PatrolPointViewSet(viewsets.ModelViewSet):
	model=PatrolPoint
	#We must provide the serializer that will give data
	#So lets go and create a serializer for Perimeter model
	serializer_class = PatrolPointSerializer
	queryset = PatrolPoint.objects.all()