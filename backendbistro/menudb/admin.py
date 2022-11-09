from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import MenuItem
from .models import Category
from .models import Cuisine

class MenuItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(MenuItem, MenuItemAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)


class CuisineAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cuisine, CuisineAdmin)