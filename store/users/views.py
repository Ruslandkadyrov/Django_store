from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
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
        return redirect('users:profile')
    return render(request, 'users/profile.html', {'user': user})


def users_cart(request):
    return render(request, 'users/cart.html')
