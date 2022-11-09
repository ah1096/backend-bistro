from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<varchar:title>/', views.detail, name='detail')
]