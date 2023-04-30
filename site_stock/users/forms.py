from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.conf import settings
from captcha.fields import CaptchaField
from django.forms import ValidationError



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


class CustomPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your old password'
    }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your new password'
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat new password'
    }))

    def clean(self):
        cleaned_data = super().clean()
        user = self.user
        new = cleaned_data.get('new_password1')
        if user.check_password(new):
            raise ValidationError('You are entering the old password')