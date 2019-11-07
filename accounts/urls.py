from django.conf.urls import url, include
from django.urls import path
from accounts.views import HomeView,GuardsView,RemoveGuardsView


app_name="accounts"

urlpatterns=[
    path('home/',HomeView.as_view(),name="home"),
	path('guards/',GuardsView.as_view(),name="guards"),
	url(r'^remove_guards/(?P<pk>[0-9A-Fa-f-]+)/$',RemoveGuardsView.as_view(),name="remove_guards"),
]