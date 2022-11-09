from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.FloatField(default=None)
    category_id = models.ForeignKey('Category', default=None, on_delete=models.PROTECT)
    cuisine_id = models.ForeignKey('Cuisine', default=None, on_delete=models.PROTECT)

    def __str__(self):
        return self.title + ": " + str(self.description) + " ($" + str(self.price) + ")"

class Category(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

class Cuisine(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label
