from django.shortcuts import render
from django.views.generic import DetailView
from perimeters.models import Perimeter
from .models import Patrol

# Create your views here.

class PerimeterPatrolsView(DetailView):
	"""docstring for ClassName"""
	template_name = "perimeter_patrols.html"
	model = Perimeter

	def get_context_data(self, **kwargs):
	    context = super(PerimeterPatrolsView, self).get_context_data(**kwargs)
	    return context

class PatrolView(DetailView):
	template_name = "patrols_view.html"
	model = Patrol

	def get_context_data(self, **kwargs):
	    context = super(PatrolView, self).get_context_data(**kwargs)
	    return context

# class PatrolPoints():