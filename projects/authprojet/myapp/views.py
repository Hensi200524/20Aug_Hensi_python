from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout

# Create your views here.
def index(request):
    msg=""
    if request.method=='POST':
        unm=request.POST["email"]
        pas=request.POST["password"]

        user=Userregister.objects.filter(email=unm,password=pas)
        if user:#TRUE
            print("login successfully!")
            msg="login sucess!"

            request.session["user"]=unm #generate session
            return redirect('home')
        else:
            print("error,login failed!")
            msg="login Failed..."
    return render(request,'index.html',{'msg':msg})

def register(request):
    msg=""
    if request.method == 'POST':
        email = request.POST["email"]
        form=registerfrom(request.POST)
        if form.is_valid():
            if Userregister.objects.filter(email=email).exists():
                msg = "Email is already exists!"
            else:
                form.save()
                print("register successfully")
                return redirect("/")
        else:
            print(form.errors)
    return render(request,'register.html',{'msg':msg})

def home(request):
    user = request.session.get("user")
    # print(cuser.fullname)
    try:
        cuser=Userregister.objects.get(email=user)
        return render(request,'home.html',{'userc':cuser.fullname})
    except Userregister.DoesNotExist:
        print("Error")
    return render(request,'home.html')

def userlogout(request):
    logout(request)
    return redirect('/')
