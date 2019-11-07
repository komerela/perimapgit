from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import Floor
from django.http import HttpResponseRedirect
from django.urls import reverse
from perimeters.models import Perimeter
from .forms import FloorCreateForm

# Create your views here.


class CreateFloorView(CreateView):
	template_name = "create_floor.html"
	form_class=FloorCreateForm

	def get_initial(self):
		perimeter=Perimeter.objects.get(pk=self.kwargs['pk'])
		return {"perimeter":perimeter}
	def get_context_data(self, **kwargs):
		context = super(CreateFloorView, self).get_context_data(**kwargs)
		context['perimeter'] = Perimeter.objects.get(pk=self.kwargs['pk'])
		return context

	def form_valid(self,form):
		floor=form.save()
		return HttpResponseRedirect(self.get_success_url(floor.perimeter.id))
	def get_success_url(self,pk=None):
		return reverse("perimeters:view",kwargs={'pk':pk})

class EditFloorView(UpdateView):
	template_name = "create_floor.html"
	model = Floor
	fields=['name']

	def get_object(self):
		return Floor.objects.get(pk=self.kwargs['pk'])

class DeleteFloorView(DeleteView):

	template_name = "delete_floor.html"
	model = Floor
	fields=['name']

	def delete(self, request, *args, **kwargs):
		floor = self.get_object()
		pk=floor.perimeter.id
		floor.delete()
		return HttpResponseRedirect(self.get_success_url(pk))


	def get_success_url(self,pk=None):
		return reverse("perimeters:view",kwargs={'pk':pk})


	def get_object(self):
		return Floor.objects.get(pk=self.kwargs['pk'])
