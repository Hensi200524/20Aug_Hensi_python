from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
       contact= ContactForm(request.POST)
       if contact.is_valid():
            contact.save()
            print("record inserted!")
       else:
            print(contact.errors)
    return render(request,'contact.html')

def showdata(request):
    data = contactinfo.objects.all()
    return render(request,'showdata.html',{'data':data})

def deletedata(request,id):
    cid = contactinfo.objects.get(id=id)
    contactinfo.delete(cid)
    return redirect("showdata")
    


