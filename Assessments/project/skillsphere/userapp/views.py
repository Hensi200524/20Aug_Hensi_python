from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    msg = ""
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = Usersignup.objects.get(email=email, password=password)
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                return redirect('/')   # success
            except Usersignup.DoesNotExist:
                msg = "Invalid email or password ❌"

    return render(request, 'login.html', {'msg': msg, 'form': form})


def signup(request):
     if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
     else:
        form = UserSignupForm()
     return render(request,'signup.html')

def courses(request):
    return render(request,'courses.html')

def course_detail(request):
    return render(request,'course_detail.html')

def my_courses(request):
    return render(request,'my_courses.html')

def profile(request):
    return render(request,'profile.html')