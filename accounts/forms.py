from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.Form):
    password2 = forms.CharField(label='Confirm Password',
                                max_length=50, min_length=5,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
