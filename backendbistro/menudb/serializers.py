from django.contrib.auth.models import User, Group
from rest_framework import serializers
from menudb.models import MenuItem, Cuisine, Category

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class MenuItemSerializer(serializers.HyperlinkedModelSerializer):

    category_id = CategorySerializer()
    cuisine_id = CuisineSerializer()
    
    class Meta:
        model = MenuItem
        fields = ['title', 'description', 'price', 'category_id', 'cuisine_id']
