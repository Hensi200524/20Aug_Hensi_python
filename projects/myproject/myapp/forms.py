from django import forms
from .models import *

class Contactform(forms.ModelForm):
    class Meta:
        model = contactinfo
        fields = '__all__'