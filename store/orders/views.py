from django.shortcuts import render

from cart.utils import get_user_carts


def create_order(request):
    user_cart = get_user_carts(request)
    return render(request, 'orders/create_order.html', {"carts": user_cart})
