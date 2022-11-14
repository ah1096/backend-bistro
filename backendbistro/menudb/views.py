from django.shortcuts import render
from django.http import HttpResponse
from .models import MenuItem, Category, Cuisine
from django.http import JsonResponse

#FOLLOWING 4 LINES ADDED FROM Django REST framework quick start tutorial///////////
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from backendbistro.menudb.serializers import UserSerializer, GroupSerializer

#VIEWS = request handler, NOT necessarily visible to user

def index(request):
    return HttpResponse("Hello, world. You're at the menudb index.")

def get_menu(request):
    menu = list(MenuItem.objects.values('title', 'description', 'price', 'category_id_id__label', 'cuisine_id_id__label'))
    return JsonResponse(menu, safe=False)

#ADDED FROM Django REST framework quick start tutorial///////////

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

