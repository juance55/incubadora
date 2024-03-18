from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.inicio, name='inicio'),
    path('list_registro/', views.list_registro, name='list_registro'),
    path('formulario/', views.formulario, name="formulario")
]
