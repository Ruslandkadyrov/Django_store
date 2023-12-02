from django.urls import path
from myapp.views import index, contact, index_item, cart, categories, product


app_name = 'myapp'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', index_item, name='detail'),
    path('contact/', contact, name='contact'),
    path('cart/', cart, name='cart'),
    path('categories/', categories, name='categories'),
    path('product/', product, name='product')
]
 