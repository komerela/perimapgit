from rest_framework import viewsets
from .serializers import CustomUserSerializer
from .models import CustomUser


# ViewSets define the view behavior. Handles requests
class CustomUserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer