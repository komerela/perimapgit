from django.conf.urls import url, include
from django.urls import path
from .views import CreateFloorView

app_name="floors"

urlpatterns=[
    url(r'^create/(?P<pk>[0-9A-Fa-f-]+)/$',CreateFloorView.as_view(),name="create"),

]