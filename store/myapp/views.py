from django.shortcuts import redirect, render
from .models import Category, Product, Subcategory, Size


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


def clothes(request):
    category_clothing = Category.objects.get(name='Одежда')
    subcategories_clothing = Subcategory.objects.filter(category=category_clothing)
    subcategory_ids = [subcategory.id for subcategory in subcategories_clothing]
    subcategorys = Subcategory.objects.filter(id__in=subcategory_ids)
    items = Product.objects.filter(subcategory__id__in=subcategory_ids)
    sizes = Size.objects.all()
    context = {
        'items': items,
        'subcategorys': subcategorys,
        'sizes': sizes,
    }
    return render(request, "myapp/clothes.html", context)


def accessories(request):
    category_clothing = Category.objects.get(name='Аксессуары')
    subcategories_clothing = Subcategory.objects.filter(category=category_clothing)
    subcategory_ids = [subcategory.id for subcategory in subcategories_clothing]
    items = Product.objects.filter(subcategory__id__in=subcategory_ids)
    context = {
        'items': items
    }
    return render(request, "myapp/accessories.html", context)


def lingerie(request):
    category_clothing = Category.objects.get(name='Женское белье')
    subcategories_clothing = Subcategory.objects.filter(category=category_clothing)
    subcategory_ids = [subcategory.id for subcategory in subcategories_clothing]
    items = Product.objects.filter(subcategory__id__in=subcategory_ids)
    context = {
        'items': items
    }
    return render(request, "myapp/lingerie.html", context)


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
