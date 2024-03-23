from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from django.contrib.auth.views import LoginView, LogoutView


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"{user.username}, Вы зарегестрировались")
            return redirect("myapp:index")
    form = NewUserForm()
    context = {'form': form}
    return render(request, 'users/checkout.html', context)

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.contact_number = request.POST.get('contact_number')
        user.town = request.POST.get('town')
        user.adress = request.POST.get('adress')
        user.save()
        messages.success(request, "Профиль успешно обнавлен")
        return redirect('users:profile')
    return render(request, 'users/profile.html', {'user': user})


def users_cart(request):
    return render(request, 'users/cart.html')


class CustomLoginView(LoginView):
    def get_success_url(self):
        url = super().get_success_url()
        messages.success(self.request, f"Добро пожаловать, {self.request.user.username}!")
        return url


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, "Вы успешно вышли из системы.")
        return super().dispatch(request, *args, **kwargs)
