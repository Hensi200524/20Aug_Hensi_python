from django import forms
from .models import Member
from .models import Complaint

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'flat_no', 'contact', 'email']

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['title', 'category', 'description', 'image']