from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms


class NewUserForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    contact_number = forms.CharField(required=True)
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'contact_number',
            'password1',
            'password2'
        )


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = CustomUser
        fields = ['contact_number', 'password']

    contact_number = forms.CharField()
    password = forms.CharField()
    username = forms.CharField(required=False)
