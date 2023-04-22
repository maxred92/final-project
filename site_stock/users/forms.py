from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.conf import settings
from captcha.fields import CaptchaField



class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2')
    
    
    captcha = CaptchaField()

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your first name'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password'
    }))


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password'
    }))