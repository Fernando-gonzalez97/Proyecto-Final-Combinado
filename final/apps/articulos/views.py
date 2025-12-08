from django.shortcuts import render
from .models import Articulo
from django.views.generic import ListView, DetailView


# def ArticuloView(request):
#    articulos = Articulo.objects.all()
#    return render(request, 'articulos.html', {'articulos': articulos})

class ArticuloListView(ListView):
     model = Articulo
     template_name = 'articulos.html'
     context_object_name = 'articulos'


class ArticuloDetailView(DetailView):
     model = Articulo
     template_name = 'articulo_individual.html'
     context_object_name = 'articulos'
     pk_url_kwarg = 'id'
     queryset = Articulo.objects.all()


