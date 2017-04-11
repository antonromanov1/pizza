from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Meal(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Pizza(Meal): pass

class Hot(Meal): pass

class Salads(Meal): pass

class Drinks(Meal): pass

class Desserts(Meal): pass




@python_2_unicode_compatible
class PizzaHot(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
