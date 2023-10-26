from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from APP_settings.models import UserForm

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password1 = forms.CharField(max_length=20, min_length=8)

    username.widget.attrs.update({'placeholder': 'username'})
    email.widget.attrs.update({'placeholder': 'e-mail'})
    password1.widget.attrs.update({'placeholder': 'password'})
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(max_length=20, min_length=8)

    username.widget.attrs.update({'placeholder': 'username'})
    password1.widget.attrs.update({'placeholder': 'password'})
    