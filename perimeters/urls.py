from django.conf.urls import url, include
from django.urls import path
from .views import PerimetersView,PerimeterCreateView,PerimeterDetailQrView,PerimeterDetailView,PerimeterDetailMapView


app_name="perimeters"

urlpatterns=[
    path('',PerimetersView.as_view(),name="all"),
    path('create/',PerimeterCreateView.as_view(),name="create"),
    url(r'^view/(?P<pk>[0-9A-Fa-f-]+)/$',PerimeterDetailView.as_view(),name="view"),
    url(r'^map_view/(?P<pk>[0-9A-Fa-f-]+)/$',PerimeterDetailMapView.as_view(),name="map_view"),
    url(r'^qr_view/(?P<pk>[0-9A-Fa-f-]+)/$',PerimeterDetailQrView.as_view(),name="qr_view"),


]