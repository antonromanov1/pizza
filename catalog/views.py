from django.shortcuts import render
from models import Meal, Pizza, Hot, Salads, Desserts, Drinks

def index(request):
    pizzas = Pizza.objects.all()
    hots = Hot.objects.all()[:2]
    return render(request, "catalog/index.html", {"pizzas" : pizzas, "hots" : hots})

def pizza(request):
    return render(request, "catalog/pizza.html", {})

def hot(request):
    return render(request, "catalog/hot.html", {})

def salads(request):
    return render(request, "catalog/salads.html", {})

def drinks(request):
    return render(request, "catalog/drinks.html", {})

def desserts(request):
    return render(request, "catalog/desserts.html", {})
