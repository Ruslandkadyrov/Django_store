from django.urls import path
from myapp.views import index, contact, cart, clothes, product, add_product, update_product, accessories, lingerie


app_name = 'myapp'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('cart/', cart, name='cart'),
    path('clothes/', clothes, name='clothes'),
    path('accessories/', accessories, name='accessories'),
    path('lingerie/', lingerie, name='lingerie'),
    path('product/<int:id>/', product, name='product'),
    path('add_product/', add_product, name='add_product'),
    path('update_product/<int:product_id>/', update_product, name='update_product')
]
