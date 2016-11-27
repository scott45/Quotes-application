from django import forms
from .models import Quote
from django.contrib.auth.models import User


class StoreForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ('title', 'description')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
