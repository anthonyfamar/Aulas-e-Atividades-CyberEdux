from django.urls import path
from cadastramento import views

urlpatterns = [
    path('', views.index),
    path('cadastro', views.cadastro),
    path('tabela', views.tabela)
]