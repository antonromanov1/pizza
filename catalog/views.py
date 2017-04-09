from django.shortcuts import render

def index(request):
    return render(request, "catalog/index.html", {})

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
