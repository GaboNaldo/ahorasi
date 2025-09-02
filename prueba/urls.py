from django.urls import path
from prueba import views


urlpatterns = [
    path('', views.hola, name='hola'),
]