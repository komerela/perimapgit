from rest_framework import viewsets
from .serializers import FloorSerializer
from .models import Floor

class FloorViewSet(viewsets.ModelViewSet):
	model=Floor
	#We must provide the serializer that will give data
	#So lets go and create a serializer for Perimeter model
	serializer_class = FloorSerializer
	queryset = Floor.objects.all()