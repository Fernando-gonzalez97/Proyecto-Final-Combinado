from django.urls import path
from .views import ArticuloListView, ArticuloDetailView

urlpatterns = [
    path('articulos/', ArticuloListView.as_view(), name='articulos'),
    path('articulos/<int:id>/', ArticuloDetailView.as_view(), name= 'articulo_individual')
]