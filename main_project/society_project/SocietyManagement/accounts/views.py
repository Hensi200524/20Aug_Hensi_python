from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
from adminpanel.models import MemberApproval
from django.contrib import messages

# Create your views here.
def dashboard(request):
    username = request.session.get('username', None)  # fetch username from session
    return render(request, 'dashboard.html',{'username': username})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == "admin" and password == "admin@123":
            messages.success(request, "Welcome Admin")
            return redirect("admin_dashboard")

        user = Usersignup.objects.filter(username=username, password=password).first()

        if not user:
            messages.error(request, "Invalid username or password")
            return redirect('login')

        approval = MemberApproval.objects.filter(user=user).first()

        if not approval or approval.status != "Approved":
            messages.error(request, "Admin has not approved your account yet")
            return redirect('login')

        # ⭐ SAVE IN SESSION
        request.session['user_id'] = user.id
        request.session['username'] = user.username

        messages.success(request, "Login Successful")
        return redirect('member_dashboard')

    return render(request, "login.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        house = request.POST['house']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # ---- CHECK MATCH ----
        if password != confirm_password:
            messages.error(request, " Please Enter Password & Confirm Password are same!")
            return render(request, "signup.html")

        # ---- SAVE USER ----
        user = Usersignup.objects.create(
            username=username,
            email=email,
            phone=phone,
            house=house,
            password=password,
            confirm_password=confirm_password
        )

        MemberApproval.objects.create(user=user)

        messages.success(request, "Signup successful! Wait for admin approval.")
        return redirect("login")

    return render(request, "signup.html")

def userlogout(request):
    logout(request)
    return redirect('login')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('/')
        else:
            messages.error(request, "Something went wrong! Try again.")
    else:
        form = ContactForm()
    return render(request,'contact.html',{"form": form})


    
