from django.conf.urls import url, include
from django.urls import path
from accounts.views import RegisterView,HomeView,GuardsView


app_name="accounts"

urlpatterns=[
    path('home/',HomeView.as_view(),name="home"),
	path('guards/',GuardsView.as_view(),name="guards"),
]