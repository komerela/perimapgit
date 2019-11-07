from django.conf.urls import url, include
from django.urls import path
from .views import CreateCheckpointView,FloorCheckpointsView,DeleteCheckpointView

app_name="checkpoints"

urlpatterns=[
    url(r'^create/(?P<pk>[0-9A-Fa-f-]+)/$',CreateCheckpointView.as_view(),name="create"),
    url(r'^floor_checkpoints/(?P<pk>[0-9A-Fa-f-]+)/$',FloorCheckpointsView.as_view(),name="floor_checkpoints"),
    url(r'^delete/(?P<pk>[0-9A-Fa-f-]+)/$',DeleteCheckpointView.as_view(),name="delete"),

]