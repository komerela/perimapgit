from django.shortcuts import render
from django.views.generic import CreateView,DeleteView
from .models import CheckPoint
from .forms import CheckpointCreateForm
from perimeters.models import Perimeter
from django.http import HttpResponseRedirect
from django.urls import reverse
from json_views.views import JSONListView
from floors.models import Floor


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

	def get_form(self, form_class=None):
		form = super(CreateCheckpointView, self).get_form(form_class)
		form.fields['floor'].queryset = Floor.objects.filter(perimeter=self.kwargs['pk'])
		return form

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

class DeleteCheckpointView(DeleteView):
	template_name = "delete_checkpoint.html"
	model = CheckPoint

	def delete(self, request, *args, **kwargs):
		cp = self.get_object()
		pk=cp.perimeter.id
		cp.delete()
		return HttpResponseRedirect(self.get_success_url(pk))


	def get_success_url(self,pk=None):
		return reverse("perimeters:view",kwargs={'pk':pk})

	def get_object(self):
		return CheckPoint.objects.get(pk=self.kwargs['pk'])




	

