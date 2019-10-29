from django.conf.urls import url, include
from django.urls import path
from .views import PerimeterPatrolsView,PatrolView

app_name="patrol"

urlpatterns=[
    url(r'^view/(?P<pk>[0-9A-Fa-f-]+)/$',PerimeterPatrolsView.as_view(),name="view"),
    url(r'^detail_view/(?P<pk>[0-9A-Fa-f-]+)/$',PatrolView.as_view(),name="detail_view"),

]