# from django.forms import ModelForm
from django import forms   #insert style into forms
from .models import *

class product_form(forms.ModelForm):
    
    class Meta:
        model = product
        fields = '__all__'
        
        widgets={
            'product_name' : forms.TextInput(attrs={'class':'form-control'}),
            'product_code' : forms.TextInput(attrs={'class':'form-control'}),
            'price' : forms.NumberInput(attrs={'class':'form-control'}),
            'gst' : forms.NumberInput(attrs={'class':'form-control'}),
            'count' : forms.NumberInput(attrs={'class':'form-control'})
        }
        
        