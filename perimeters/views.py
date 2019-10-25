from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView
from .models import Perimeter
from .forms import PerimeterForm
from django.urls import reverse
from floors.models import Floor
from checkpoint.models import CheckPoint

# Create your views here.
class PerimetersView(ListView):
    template_name = "perimeters.html"
    model = Perimeter

class PerimeterCreateView(CreateView):
	template_name = "create_perimeters.html"
	model = Perimeter
	from_class=PerimeterForm
	fields=['name',]

	def form_valid(self,form):
		perimeter = form.save(commit=False)
		perimeter.user = self.request.user
		perimeter.save()
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('perimeters:all')

class PerimeterDetailView(DetailView):
	template_name = "view_perimeters.html"
	model = Perimeter

	def get_context_data(self, **kwargs):
	    context = super(PerimeterDetailView, self).get_context_data(**kwargs)
	    perimeter = Perimeter.objects.get(pk = self.kwargs['pk'])
	    context['checkpoints'] = CheckPoint.objects.filter(perimeter=perimeter)
	    context['floors'] = Floor.objects.filter(perimeter=perimeter)

	    return context

