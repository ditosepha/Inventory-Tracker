from django import forms
from .models import Item

class AddItem(forms.ModelForm):
    price = forms.DecimalField(decimal_places=2, max_digits=10)
    class Meta:
        model = Item
        fields = ['name', 'serial_number', 'price']
        widgets = {
            'item Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item Name'}),
            'serial Number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Serial Number'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
        }