from rest_framework import viewsets
from .serializers import PatrolSerializer
from .models import Patrol
from rest_framework.response import Response


class PatrolViewSet(viewsets.ModelViewSet):
	model=Patrol
	#We must provide the serializer that will give data
	#So lets go and create a serializer for Perimeter model
	serializer_class = PatrolSerializer
	queryset = Patrol.objects.all()

	def list(self, request):
		queryset = Patrol.objects.all()
		if(request.GET.get('perimeter')):
			queryset=Patrol.objects.filter(perimeter=request.GET.get('perimeter'))

		serializer = PatrolSerializer(queryset,many=True)
		return Response(serializer.data)
