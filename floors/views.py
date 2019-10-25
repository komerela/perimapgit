from django.shortcuts import render
from django.views.generic import CreateView
from .models import Floor
from django.http import HttpResponseRedirect
from django.urls import reverse
from perimeters.models import Perimeter

# Create your views here.


class CreateFloorView(CreateView):
    template_name = "create_floor.html"
    model = Floor
    fields = ['name','perimeter']

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