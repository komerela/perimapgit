from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth import authenticate, login
from perimeters.models import Perimeter
from django.urls import reverse
from django.views.generic.base import RedirectView
from django.shortcuts import render, redirect



# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accounts:home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


class HomeView(TemplateView):
	template_name = "home/dashboard.html"

class GuardsView(ListView):
	template_name = "home/guards.html"
	model = CustomUser
	def get_queryset(self):
		return CustomUser.objects.filter(guard_for=self.request.user)

class RemoveGuardsView(RedirectView):
	permanent = False
	def get_redirect_url(self, *args, **kwargs):
		user = CustomUser.objects.get(pk=kwargs['pk'])
		user.guard_for=None
		user.save()
		return reverse('accounts:guards')


		
