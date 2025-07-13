# data/forms.py
from django import forms
from .models import Product

class adding_content(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','price','media_file'] # Add media_file