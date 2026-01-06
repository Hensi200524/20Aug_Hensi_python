from django import forms
from .models import *

class UsersignupForm(forms.ModelForm):
    class Meta:
        model = Usersignup
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']