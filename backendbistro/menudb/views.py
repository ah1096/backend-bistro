from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the menudb index.")

def detail(request, title):
    return HttpResponse("You're looking at the menu item: %s." % question_id)


