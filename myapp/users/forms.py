from django import forms
from .models import Users


class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200)
    email = forms.EmailField(label='Email', max_length=200)