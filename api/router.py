from rest_framework import routers
from accounts.viewsets import CustomUserViewset
from perimeters.viewsets import PerimetersViewSet
from patrolpoint.viewsets import PatrolPointViewSet
from checkpoint.viewsets import CheckPointViewSet
from floors.viewsets import FloorViewSet
from patrol.viewsets import PatrolViewSet

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewset)
router.register(r'perimeters', PerimetersViewSet)
router.register(r'patrolpoint', PatrolPointViewSet)
router.register(r'checkpoint', CheckPointViewSet)
router.register(r'floors', FloorViewSet)
router.register(r'patrol', PatrolViewSet)