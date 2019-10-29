from rest_framework import viewsets
from .serializers import PerimeterSerializer
from .models import Perimeter
from rest_framework.decorators import action
from rest_framework.response import Response



class PerimetersViewSet(viewsets.ModelViewSet):
	model=Perimeter
	#We must provide the serializer that will give data
	#So lets go and create a serializer for Perimeter model
	serializer_class = PerimeterSerializer
	queryset = Perimeter.objects.all()

	@action(detail=False, methods=['get'])
	def guard(self, request, pk=None):
		user=self.request.user
		print(user)
		if(user.guard_for):
			user=user.guard_for
		perimeters = Perimeter.objects.filter(user=user)
		serializer=PerimeterSerializer(perimeters,many=True)
		return Response(serializer.data)

