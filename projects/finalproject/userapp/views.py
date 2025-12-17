from django.shortcuts import render,redirect
from .forms import * 
from django.core.mail import send_mail
from finalproject import settings
import random
from django.contrib.auth import logout


# Create your views here.
def index(request):
    user = request.session.get('email')
    try:
        unm=Usersignup.objects.get(email=user)
        return render(request,'index.html',{'uname':unm.fname})
    except Usersignup.DoesNotExist:
        print("Error")
    return render(request,'index.html')

    # return render(request,'index.html',{'user':user})

def about(request):
    user = request.session.get('email')
    return render(request,'about.html',{'user':user})

def contact(request):
    user = request.session.get('email')
    if request.method=='POST':
        contact=Contactform(request.POST)
        if contact.is_valid():
            contact.save()
            print("Contact Successfully!")
            return redirect("/")
        else:
            print(contact.errors)
    return render(request,'contact.html',{'user':user})

def login(request):
    msg=""
    if request.method=='POST':
        em=request.POST["email"]
        pas=request.POST["password"]

        user=Usersignup.objects.filter(email=em,password=pas)
        userid = Usersignup.objects.get(email=em)
        print("UserId",userid)
        if user:
            print("Login Successfully!")
            msg="Login successfully!"
            request.session["email"]=em #session generte
            request.session["userid"]=userid.id
            return redirect("/")
        else:
            print("Login Failed...!")
            msg="Login Failed!"
    return render(request,'login.html')

def notes(request):
    try:
        user = request.session.get('email')
        unm = Usersignup.objects.get(email=user)
        if request.method=='POST':
            newreq=Notesform(request.POST,request.FILES)
            if newreq.is_valid():
                x=newreq.save(commit=False)
                x.user=unm
                x.status="Pending"
                x.save()
                print("Notes Submitted!")
                return redirect("/")
            else:
                print(newreq.errors)
    except:
        print("error")
    return render(request,'notes.html',{'user':user})

def profile(request):
    user = request.session.get('email')
    userid = request.session.get('userid')
    cuser= Usersignup.objects.get(id=userid)
    if request.method=='POST':
        updateReq=Updateform(request.POST,instance=cuser)
        if updateReq.is_valid():
            updateReq.save()
            print("Profile Updated!")
            return redirect("/")
        else:
            print(updateReq.errors)
    return render(request,'profile.html',{'user':user,'cuser':cuser})

def sign_up(request):
    if request.method=='POST':
        signup=Signupform(request.POST)
        if signup.is_valid():
            signup.save()
            print("Register Successfully!")

            #Email sending code
            global otp
            otp=random.randint(1111,9999)
            sub="Your One Time Password!"
            msg=f"Dear User\n\nThanks for registration with us!\nFor Verification, your one time password is {otp}.\n\nThanks & Regards!\nNotesApp Team\n+91 9773077345 | www.tops-int.com"
            from_ID=settings.EMAIL_HOST_USER
            to_ID=[request.POST['email']]

            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)

            return redirect("otpverify")
        else:
            print(signup.errors)
    return render(request,'sign_up.html')

def otpverify(request):
    msg=""
    if request.method=='POST':
        if request.POST["otp"]==str(otp):
            print("Verification successfully!")
            msg="verification success!"
            return redirect("login")
        else:
            print("Error!verification is not proper!")
            msg="verification lost!"
    return render(request,'otpverify.html',{'msg':msg})

def userlogout(request):
    logout(request)
    return redirect("login")



