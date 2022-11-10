from django.shortcuts import render
from django.http import HttpResponse
from .models import MenuItem, Category, Cuisine
from django.http import JsonResponse

#VIEWS = request handler, NOT necessarily visible to user

def index(request):
    return HttpResponse("Hello, world. You're at the menudb index.")

def get_menu(request):
    menu = list(MenuItem.objects.values('title', 'description', 'price', 'category_id_id__label', 'cuisine_id_id__label'))
    return JsonResponse({'Menu': menu})



