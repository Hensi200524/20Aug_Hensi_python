from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        user=SignupForm(request.POST)
        if user.is_valid():
            user.save()
            print("User Registerd!")
            return redirect("login")
        else:
            print(user.errors)
    return render(request,'signup.html')
