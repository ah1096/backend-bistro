from django.urls import path, include
from . import views

#ADDED FROM Django REST framework tutorial
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('get_menu/', views.get_menu, name='get_menu'), 
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

