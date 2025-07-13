from django.forms import ModelForm
from . models import MovieInformation
class MovieForm(ModelForm):
    class Meta: ##Meta is using for description the main class 
        model=MovieInformation
        fields='__all__'