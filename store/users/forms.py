from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms


class NewUserForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    contact_number = forms.CharField(required=True)
    town = forms.CharField(required=True)
    adress = forms.CharField(required=True)
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'email',
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
