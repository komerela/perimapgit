from rest_framework import viewsets
from .serializers import CheckPointSerializer
from .models import CheckPoint

class CheckPointViewSet(viewsets.ModelViewSet):
	model=CheckPoint
	#We must provide the serializer that will give data
	#So lets go and create a serializer for Perimeter model
	serializer_class = CheckPointSerializer
	queryset = CheckPoint.objects.all()