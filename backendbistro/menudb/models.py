from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    #category_id = models.ForeignKey('Category', on_delete=models.PROTECT)
    #cuisine_id = models.ForeignKey('Cuisine', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Category(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

class Cuisine(models.Model):
    label = models.CharField(max_length=100)
