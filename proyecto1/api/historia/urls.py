from django.urls import path
from . import views
urlpatterns = [
    path('api/historia/', views.HistoriaListCreate.as_view() ),
]