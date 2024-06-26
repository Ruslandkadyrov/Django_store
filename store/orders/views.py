from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render

from cart.models import Cart

from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem
from cart.utils import get_user_carts
from myapp.models import ProductSizeQty


@login_required
def create_order(request):
    user_cart = get_user_carts(request)
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)
                    if cart_items.exists():
                        # Создать заказ
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )
                        # Создать заказанные товары
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.price
                            quantity = cart_item.quantity
                            size = cart_item.size
                            try:
                                product_size_qty = product.product_size_qty.get(size=size)
                            except ProductSizeQty.DoesNotExist:
                                raise ValidationError(f'Невозможно найти товар с размером {size}')

                            size_qty = product_size_qty.quantity
                            if size_qty < quantity:
                                raise ValidationError(f'Недостаточное количество товара {name} на складе\
                                                       В наличии - {size_qty}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                                size=size,
                            )
                            size_qty -= quantity
                            product_size_qty.quantity = size_qty
                            product_size_qty.save()
                            if size_qty == 0:
                                product_size_qty.delete()


                        # Очистить корзину пользователя после создания заказа
                        cart_items.delete()

                        messages.success(request, 'Заказ оформлен!')
                        return redirect('users:users_cart')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('orders:create_order')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'phone_number': request.user.contact_number,
            }

        form = CreateOrderForm(initial=initial)

    context = {
        'form': form,
        'orders': True,
        'carts': user_cart,
    }
    return render(request, 'orders/create_order.html', context=context)