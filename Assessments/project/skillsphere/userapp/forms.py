from django import forms
from .models import *

class SignupForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['username', 'email', 'password', 'role']
