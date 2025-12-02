from django.shortcuts import render
from .forms import *

# Create your views here.
def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        contact = Contactform(request.POST)
        if contact.is_valid():
            contact.save()
            print("Insered successfully!")
        else:
            print(contact.errors)
    return render(request,'contact.html')

def index(request):
    return render(request,'index.html')

def service(request):
    return render(request,'service.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')

def showdata(request):
    data = contactinfo.objects.all()
    return render(request,'showdata.html',{'data':data})

def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')
