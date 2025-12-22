from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from adminapp.models import Course
from django.contrib import messages
from django.contrib.auth import logout
from django.core.mail import send_mail
from .models import Signup
import random
import string

# Create your views here.

def home(request):
    return render(request, 'home.html')

def courses(request):
     courses = Course.objects.all().order_by('-id')
     return render(request, 'courses.html',{'courses':courses})

def login(request):
    msg = ""
    if request.method == 'POST':
        unm = request.POST.get("username")
        pas = request.POST.get("password")

        # Try to get the user safely
        user = Signup.objects.filter(username=unm, password=pas).first()

        if user:
            # Login success → create session
            request.session["username"] = user.username
            request.session["userid"] = user.id
            msg = "Login successfully!"
            return redirect("courses")  # redirect to home/dashboard
        else:
            msg = "Login failed! Invalid username or password."

    return render(request, 'login.html', {'msg': msg})


def signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = Signupform()
    return render(request, 'signup.html')

def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'course_detail.html', {'course': course})

def enroll_course(request, id):
    if not request.session.get("userid"):
        messages.error(request, "Please login first")
        return redirect("login")

    student = Signup.objects.get(id=request.session["userid"])
    course = Course.objects.get(id=id)

    # Already enrolled check
    exists = Enrollment.objects.filter(student=student, course=course).exists()
    if exists:
        messages.warning(request, "You are already enrolled in this course")
        return redirect("payment", id=course.id)

    # Save enrollment
    Enrollment.objects.create(student=student, course=course)
    messages.success(request, "Enrollment Successful 🎉")

    # 👉 Redirect to payment page
    return redirect("payment", id=course.id)



def my_courses(request):
    student = Signup.objects.get(id=request.session["userid"])
    enrollments = Enrollment.objects.filter(student=student)
    return render(request, "my_courses.html", {"enrollments": enrollments})

def user_logout(request):
    logout(request)
    return redirect('home')

def user_profile(request):
    if not request.session.get("userid"):
        messages.error(request, "Please login first")
        return redirect("login")

    user = Signup.objects.get(id=request.session["userid"])

    if request.method == "POST":
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")

        if request.FILES.get("avatar"):
            user.avatar = request.FILES.get("avatar")

        user.save()
        messages.success(request, "Profile updated successfully 😊")
        return redirect("courses")

    return render(request, "user_profile.html", {"user": user})

def payment(request, id):
    course = Course.objects.get(id=id)
    return render(request, "payment.html", {"course": course})

def payment_success(request, id):
    course = Course.objects.get(id=id)
    return render(request, "payment_success.html", {"course": course})

def student_dashboard(request):
    student = Signup.objects.get(id=request.session["userid"])
    return render(request, "student_dashboard.html", {"student": student})

def password_reset(request):
    msg = ""
    if request.method == "POST":
        email = request.POST.get("email")
        user = Signup.objects.filter(email=email).first()
        if user:
            # Generate temporary password
            temp_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            user.password = temp_password
            user.save()

            # Send email
            send_mail(
                'Password Reset - SkillSphere',
                f'Your new temporary password is: {temp_password}',
                'vaghelahensi@gmail.com',  # replace with your sender email
                [user.email],
                fail_silently=False,
            )
            msg = "Temporary password sent to your email!"
            # Redirect to login page
            return redirect('login')

        else:
            msg = "Email not found!"

    return render(request, 'password_reset.html', {'msg': msg})










