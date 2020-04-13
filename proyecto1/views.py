from proyecto1.models import Historia
from proyecto1.serializers import HistoriaSerializer
from rest_framework import generics
from django.shortcuts import render, HttpResponse


class HistoriaListCreate(generics.ListCreateAPIView):
    queryset = Historia.objects.all()
    serializer_class = HistoriaSerializer

def index(request):
	return render(request, "proyectos/index.html")

def home(request):
	return render(request, "proyectos/home.html")

def about(request):
    return render(request, "proyectos/acerca_de.html")

def portfolio(request):
    return render(request, "proyectos/portafolio.html")

def contact(request):
    return render(request, "proyectos/contacto.html")