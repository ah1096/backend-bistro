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

class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['title', 'description', 'price']

class CuisineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuisine
        fields = ['label']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['label']
