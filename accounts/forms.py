from django import forms
from django.contrib.auth.forms import UserChangeForm, UsernameField, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=25,required=True)
    password=forms.CharField(widget=forms.PasswordInput)

