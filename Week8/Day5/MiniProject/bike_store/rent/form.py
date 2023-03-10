from django import forms
from .models import Customer, Vehicle

class CustomerForm(forms.ModelForm):
    model = Customer
    fields = ['name', 'email', 'phone', 'address']

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'