from django.shortcuts import render
from .models import Articulos

def listar_articulos(request):
    articulos = Articulos.objects.all()
    return render(request, 'gestor_blog/listar_articulos.html', {'articulos': articulos})
# Create your views here.
