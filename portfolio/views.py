from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
  projects = Project.objects.all() #devuelve todos los objetos del modelo de proyectos en la clase models.py
  return render(request, 'portfolio/portfolio.html', {'projects': projects})