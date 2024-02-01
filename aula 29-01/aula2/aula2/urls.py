
from django.urls import path
from myapp import views
from django.http import HttpResponse

def escrever_nome(request, meunome):
    return HttpResponse(f'Ola {meunome}!')

urlpatterns = [
    path('', views.home),
    path('nome/<str:meunome>', escrever_nome),
]
