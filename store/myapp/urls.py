from django.urls import path
from myapp.views import index, contacts, index_item


app_name = 'myapp'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', index_item, name='detail'),
    path('contacts/', contacts, name='contacts')
]
 