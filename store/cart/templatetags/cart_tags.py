from django import template

from cart.models import Cart
from cart.utils import get_user_carts


register = template.Library()


@register.simple_tag()
def user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
