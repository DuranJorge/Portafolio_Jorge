from django.contrib import admin
from django.urls import path
from . import views
#from core import *

urlpatterns = [
    #path('api/historia/', views.HistoriaListCreate.as_view() ),
    #path('prueba/', views.HistoriaListCreate.as_view() ),
    path('admin/', admin.site.urls),
    path('index/', views.index, name="index"),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contact/', views.contact, name="contact"),
    #path('about/', views.about, name="about"),
    #path('contact/', views.contact, name="contact"),
]

#Notas : Se creo superusuario para aadmin de django
#user jorgeduran7
#email jorgeduran7@outlook.es
#contraseña Admin123!#