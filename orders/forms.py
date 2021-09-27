from django import forms
from django.forms import TextInput

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city']

        widgets = {
            'first_name': TextInput(attrs={
                'placeholder': "Ім'я"
            }),
            'last_name': TextInput(attrs={
                'placeholder': "Прізвище"
            }),
            'email': TextInput(attrs={
                'placeholder': "Електронна почта"
            }),
            'phone': TextInput(attrs={
                'placeholder': "Телефон"
            }),
            'address': TextInput(attrs={
                'placeholder': "Адреса"
            }),
            'city': TextInput(attrs={
                'placeholder': "Місто"
            }),
        }
