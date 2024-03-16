from django.urls import path
from myapp.views import index, contact, cart, product, add_product, subcategorys, update_product, categorys, category_size


app_name = 'myapp'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('cart/', cart, name='cart'),
    path('category/<slug:slug>/', categorys, name='category_list'),
    path('subcategory/<slug:slug>/', subcategorys, name='subcategory_list'),
    path('category/<slug:category_slug>/size/<slug:size_slug>/',category_size, name='category_size_list'),
    path('product/<int:id>/', product, name='product'),
    path('add_product/', add_product, name='add_product'),
    path('update_product/<int:product_id>/', update_product, name='update_product')
]
