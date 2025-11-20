from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def index(request):
    return render(request,'index.html')

def service(request):
    return render(request,'service.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')
