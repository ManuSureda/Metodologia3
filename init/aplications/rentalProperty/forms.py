from django import forms
from .models import *


class reserveForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('name', 'lastName', 'email', 'totalCost')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'totalCost': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
        }

