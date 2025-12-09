from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Equipo

class EquipoListView(ListView):
    model = Equipo
    template_name = 'nosotros.html'
    context_object_name = 'staff'


class EquipoDetailView(DetailView):
    model = Equipo
    template_name = 'nosotros_individual.html'
    context_object_name = 'staff'
    queryset = Equipo.objects.all()

# Create your views here.
