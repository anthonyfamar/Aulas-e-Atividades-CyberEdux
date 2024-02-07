from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index),
    path('feed', views.feed),
    path('publicate', views.publicate)
]
