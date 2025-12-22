from django import forms
from .models import *
class UserSignupForm(forms.ModelForm):
    class Meta:
        model = Usersignup
        fields = ['username', 'email', 'password', 'role']
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
