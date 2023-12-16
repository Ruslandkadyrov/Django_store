from django.urls import path
from myapp.views import index, contact, cart, categories, product, add_product, update_product


app_name = 'myapp'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('cart/', cart, name='cart'),
    path('categories/', categories, name='categories'),
    path('product/<int:id>/', product, name='product'),
    path('add_product/', add_product, name='add_product'),
    path('update_product/<int:product_id>/', update_product, name='update_product')
]
 