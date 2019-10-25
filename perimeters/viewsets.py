from rest_framework import viewsets
from .serializers import PerimeterSerializer
from .models import Perimeter

class PerimetersViewSet(viewsets.ModelViewSet):
	model=Perimeter
	#We must provide the serializer that will give data
	#So lets go and create a serializer for Perimeter model
	serializer_class = PerimeterSerializer
	queryset = Perimeter.objects.all()
