from django.shortcuts import render
from django.http import HttpResponse

#VIEWS = request handler, NOT necessarily visible to user

def index(request):
    return HttpResponse("Hello, world. You're at the menudb index.")

def show_menu(request, id):
    return HttpResponse("You're looking at the menu items: %s" % id)


