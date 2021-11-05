from django import forms
from django.forms import TextInput, Textarea

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'comment']

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
                'placeholder': "Телефон",
                "value": "+380"
            }),
            'address': TextInput(attrs={
                'placeholder': "Адреса"
            }),
            'city': TextInput(attrs={
                'placeholder': "Місто"
            }),
            'comment': Textarea(attrs={
                'placeholder': "Коментар",
            })
        }
