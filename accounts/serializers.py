from rest_framework import routers, serializers, viewsets
from .models import CustomUser

# Serializers define the API representation.
class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url', 'username', 'email', 'is_staff', 'phone_number']