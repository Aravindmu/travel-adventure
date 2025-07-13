# data/forms.py
from django import forms
from .models import UserData

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['username_field', 'phone_number', 'media_file'] # Add media_file