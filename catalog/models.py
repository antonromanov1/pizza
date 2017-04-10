from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
