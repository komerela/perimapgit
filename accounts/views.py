from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth import authenticate, login
from perimeters.models import Perimeter
from django.urls import reverse

# Create your views here.

class RegisterView(CreateView):
	template_name="register.html"
	form_class = CustomUserCreationForm
	model = CustomUser
	def form_valid(self, form):
		user = form.save()
		user = authenticate(username=form.cleaned_data['username'],
									password=form.cleaned_data['password1'],
									)
		login(self.request,user)
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('accounts:home')


class HomeView(TemplateView):
	template_name = "home/dashboard.html"

class GuardsView(ListView):
	template_name = "home/guards.html"
	model = CustomUser
	def get_queryset(self):
		return CustomUser.objects.filter(guard_for=self.request.user)

		
