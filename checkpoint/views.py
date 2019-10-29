from django.shortcuts import render
from django.views.generic import CreateView
from .models import CheckPoint
from .forms import CheckpointCreateForm
from perimeters.models import Perimeter
from django.http import HttpResponseRedirect
from django.urls import reverse
from json_views.views import JSONListView


# Create your views here.

class CreateCheckpointView(CreateView):
	"""docstring for CreateCheckpointView"""
	form_class = CheckpointCreateForm
	template_name="create_checkpoint.html"

	def form_valid(self, form):
		checkpoint = form.save()
		return HttpResponseRedirect(self.get_success_url(checkpoint.perimeter.id))

	def get_success_url(self,pk=None):
		return reverse("perimeters:view",kwargs={'pk':pk})

	def get_initial(self):
		initial_data = super(CreateCheckpointView, self).get_initial()
		perimeter = Perimeter.objects.get(pk=self.kwargs['pk'])
		initial_data['perimeter']=perimeter
		return initial_data

	def get_context_data(self, **kwargs):
		context = super(CreateCheckpointView, self).get_context_data(**kwargs)
		context['perimeter'] = Perimeter.objects.get(pk=self.kwargs['pk'])
		return context

class FloorCheckpointsView(JSONListView):
	model=CheckPoint

	def get_queryset(self):
		return CheckPoint.objects.filter(floor=self.kwargs['pk'])




	

