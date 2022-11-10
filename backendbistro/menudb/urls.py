from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show_menu/<int:id>/', views.show_menu, name='show_menu'),
    

    
]