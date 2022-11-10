from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_menu/', views.get_menu, name='get_menu'), 
]