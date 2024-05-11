from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms


class NewUserForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'username',
            'contact_number',
            'town',
            'adress',
            'password1',
            'password2'
        )


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()
