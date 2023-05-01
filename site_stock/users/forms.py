from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.conf import settings
from captcha.fields import CaptchaField
from django.forms import ValidationError

from .models import Profile



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

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full py-1 px-3 rounded-xl border'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full py-1 px-3 rounded-xl border'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full py-1 px-3 rounded-xl border'
            })

        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'phone_number', 'photo')

        widgets = {
            'date_of_birth': forms.DateInput(attrs={
                'class': 'w-full py-1 px-3 rounded-xl border'
            }),
            'phone_number': forms.NumberInput(attrs={
                'class': 'w-full py-1 px-3 rounded-xl border'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'w-full py-1 px-3 rounded-xl border'
            })

        }