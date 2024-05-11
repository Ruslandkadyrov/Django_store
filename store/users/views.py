from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from cart.models import Cart
from .forms import NewUserForm, UserLoginForm
from django.contrib.auth.views import LogoutView


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            session_key = request.session.session_key
            user = form.instance
            auth.login(request, user)
            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
            messages.success(request, f"{user.first_name}, Вы зарегестрировались")
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
        user.contact_number = request.POST.get('contact_number')
        user.save()
        messages.success(request, "Профиль успешно обнавлен")
        return redirect('users:profile')
    return render(request, 'users/profile.html', {'user': user})


def users_cart(request):
    return render(request, 'users/cart.html')


def login(request):
    if request.method == 'POST':
        form_data = request.POST.copy()
        form_data['username'] = form_data['contact_number']  # Копируем значение из contact_number в username
        form = UserLoginForm(data=form_data)  # Передаем скорректированные данные в форму
        if form.is_valid():
            contact_number = request.POST['contact_number']
            password = request.POST['password']
            user = auth.authenticate(request=request, contact_number=contact_number, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f"{contact_number}, Вы вошли в аккаунт")

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                    
                return HttpResponseRedirect(reverse('myapp:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, "Вы успешно вышли из системы.")
        return super().dispatch(request, *args, **kwargs)
