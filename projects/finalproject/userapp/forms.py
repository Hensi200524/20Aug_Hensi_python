from django import forms
from .models import *

class Signupform(forms.ModelForm):
    class Meta:
        model = Usersignup
        fields='__all__'

class Updateform(forms.ModelForm):
    class Meta:
        model = Usersignup
        fields=['fname','lname','mobile']

class Notesform(forms.ModelForm):
    class Meta:
        model = Notesdata
        fields=['title','category','file','desc']

class Contactform(forms.ModelForm):
    class Meta:
        model = Usercontact
        fields='__all__'

