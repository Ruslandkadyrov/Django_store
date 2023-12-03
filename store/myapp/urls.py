from django.urls import path
from myapp.views import index, contact, cart, categories, product


app_name = 'myapp'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('cart/', cart, name='cart'),
    path('categories/', categories, name='categories'),
    path('product/<int:id>/', product, name='product')
]
 