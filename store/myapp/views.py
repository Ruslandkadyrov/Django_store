from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Product, Subcategory, Size, ProductSizeQty
from django.core.paginator import Paginator

NUMBER_OF_POSTS_PER_PAGE = 10


def paginator(request, product_list, number):
    paginator = Paginator(product_list, number)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


def index(request):
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request, "myapp/index.html", context)


def categorys(request, slug):
    category = get_object_or_404(Category, slug=slug)
    subcategorys = Subcategory.objects.filter(category=category)
    product_list = Product.objects.filter(subcategory__category=category)
    sizes = Size.objects.filter(product__in=product_list).distinct()
    items = paginator(request, product_list, NUMBER_OF_POSTS_PER_PAGE)
    title = category
    context = {
        'subcategorys': subcategorys,
        'items': items,
        'title': title,
        'sizes': sizes,
        'category': category,
    }
    return render(request, 'myapp/category_list.html', context)


def subcategorys(request, slug):
    subcategory = get_object_or_404(Subcategory, slug=slug)
    product_list = Product.objects.filter(subcategory=subcategory)
    items = paginator(request, product_list, NUMBER_OF_POSTS_PER_PAGE)
    title = subcategory
    context = {
        'items': items,
        'title': title,
        'subcategory': subcategory,
    }
    return render(request, 'myapp/subcategory_list.html', context)


def category_size(request, category_slug, size_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategorys = Subcategory.objects.filter(category=category)
    size = get_object_or_404(Size, slug=size_slug)
    product_list = Product.objects.filter(subcategory__in=subcategorys, sizes=size)
    items = paginator(request, product_list, NUMBER_OF_POSTS_PER_PAGE)
    title = size
    context = {
        'items': items,
        'title': title,
        'size': size,
        'category': category,
    }
    return render(request, 'myapp/size_list.html', context)


def contact(request):
    return render(request, "myapp/contact.html")


def cart(request):
    return render(request, "myapp/cart.html")


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
