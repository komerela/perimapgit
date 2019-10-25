from rest_framework import viewsets
from .serializers import PatrolSerializer
from .models import Patrol

class PatrolViewSet(viewsets.ModelViewSet):
	model=Patrol
	#We must provide the serializer that will give data
	#So lets go and create a serializer for Perimeter model
	serializer_class = PatrolSerializer
	queryset = Patrol.objects.all()