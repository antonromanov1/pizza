from django.shortcuts import render
from models import Meal, Pizza, Hot, Salads, Desserts, Drinks

def index(request):
    pizzas = Pizza.objects.all()
    hots = Hot.objects.all()[:2]
    return render(request, "catalog/index.html", {"pizzas" : pizzas, "hots" : hots})

def pizza(request):
    pizzas = Pizza.objects.all()
    return render(request, "catalog/pizza.html", {"pizzas" : pizzas})

def hot(request):
    hots = Hot.objects.all()
    return render(request, "catalog/hot.html", {"hots" : hots})

def salads(request):
    salads = Salads.objects.all()
    return render(request, "catalog/salads.html", {"salads" : salads})

def drinks(request):
    drinks = Drinks.objects.all()
    return render(request, "catalog/drinks.html", {"drinks" : drinks})

def desserts(request):
    desserts = Desserts.objects.all()
    return render(request, "catalog/desserts.html", {"desserts" : desserts})

def testing(request):
    sl = request.POST
    ls = []
    summ = 0

    for x in sl:
        if "csrf" not in str(x):
            summ += int(str(sl[x])) * int(Hot.objects.get(name=str(x)).price)
            if (str(sl[x]) != "0"):
                ls.append(Hot.objects.get(name=str(x)))

    return render(request, "catalog/testing.html", {"ls": ls, "summ" : str(summ)})

