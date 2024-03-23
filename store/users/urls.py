from django.urls import path
from .views import CustomLoginView, CustomLogoutView, profile, register, users_cart


app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('users-cart/', users_cart, name='users_cart'),
]
