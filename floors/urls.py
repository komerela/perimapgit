from django.conf.urls import url, include
from django.urls import path
from .views import CreateFloorView,EditFloorView,DeleteFloorView

app_name="floors"

urlpatterns=[
    url(r'^create/(?P<pk>[0-9A-Fa-f-]+)/$',CreateFloorView.as_view(),name="create"),
    url(r'^edit/(?P<pk>[0-9A-Fa-f-]+)/$',EditFloorView.as_view(),name="edit"),
    url(r'^delete/(?P<pk>[0-9A-Fa-f-]+)/$',DeleteFloorView.as_view(),name="delete"),


]