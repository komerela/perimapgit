from rest_framework import viewsets,status
from .serializers import PatrolPointSerializer
from .models import PatrolPoint
from rest_framework.response import Response
from checkpoint.models import CheckPoint
from patrol.models import Patrol


class PatrolPointViewSet(viewsets.ModelViewSet):
	model=PatrolPoint
	#We must provide the serializer that will give data
	#So lets go and create a serializer for Perimeter model
	serializer_class = PatrolPointSerializer
	queryset = PatrolPoint.objects.all()

	def create(self,request):
		#Check if the scanned qr code is valid
		if(request.POST.get('code')):
			try:
				checkpoint = CheckPoint.objects.get(bar_code=request.POST.get('code'))
				patrol=Patrol.objects.get(pk=request.POST.get('patrol'))
				#create a patrol point record
				obj, created = PatrolPoint.objects.update_or_create(
				    patrol=patrol, checkpoint=checkpoint,
				    defaults={'patrol':patrol,'checkpoint':checkpoint },
				)
				serializer=PatrolPointSerializer(obj,many=False)
				return Response(serializer.data)
			except Exception as e:
				print(e)
				return Response(data={"success":"false","message":"The scanned code is invalid"},status=status.HTTP_400_BAD_REQUEST)
			
		else:
			return Response(data={"success":"false","message":"Provide a scanned code"},status=status.HTTP_400_BAD_REQUEST)