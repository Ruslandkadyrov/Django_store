from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request, "myapp/index.html", context)


def index_item(request, id: int):
    item = Product.objects.get(id=id)
    context = {
        'item': item
    }
    return render(request, "myapp/detail.html", context)


def contact(request):
    return render(request, "myapp/contact.html")


def cart(request):
    return render(request, "myapp/cart.html")


def categories(request):
    return render(request, "myapp/categories.html")


def product(request):
    return render(request, "myapp/product.html")
