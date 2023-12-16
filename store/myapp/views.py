from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product

def index(request):
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request, "myapp/index.html", context)


def contact(request):
    return render(request, "myapp/contact.html")


def cart(request):
    return render(request, "myapp/cart.html")


def categories(request):
    return render(request, "myapp/categories.html")


def product(request, id: int):
    item = Product.objects.get(id=id)
    context = {
        'item': item
    }
    return render(request, "myapp/product.html", context)


def add_product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES['upload']
        item = Product(name=name, price=price, description=description, image=image)
        item.save()
    return render(request, "myapp/add_product.html")


def update_product(request, product_id: int):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        product.image = request.FILES.get('upload', product.image)
        product.save()
        return redirect('/myapp/')
    context = {'product': product}
    return render(request, 'myapp/update_product.html', context)
