from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class PaginaPrincipalArticulos(TemplateView):
    template_name = 'articulos/index.html'
