from django import forms
from .models import *

class registerfrom(forms.ModelForm):
    class Meta:
        model = Userregister
        fields = '__all__'