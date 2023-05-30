from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'es. MarioBros',
        'class': 'form-control py-2 px-3',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'form-control py-2 px-3',
    }))

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'es. MarioBros',
        'class': 'form-control py-2 px-3',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'es. mariobros@gmail.com',
        'class': 'form-control py-2 px-3',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'form-control py-2 px-3',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm your Password',
        'class': 'form-control py-2 px-3',
    }))




