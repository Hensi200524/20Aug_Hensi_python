from django import forms
from .models import *

class Signupform(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['username', 'email', 'password', 'avatar']