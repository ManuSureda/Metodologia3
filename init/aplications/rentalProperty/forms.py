from django import forms
from .models import *


class reserveForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('property', 'name', 'lastName', 'email', 'dateFrom', 'dateTo', 'totalCost')
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'dateFrom': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'dateTo': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'totalCost': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
        }

# {% csrf_token %}

# email = forms.EmailField(widget=forms.EmailInput(
#       attrs={
#           'class': 'form-control',
#           'id': 'email'
#       }
#   ))
