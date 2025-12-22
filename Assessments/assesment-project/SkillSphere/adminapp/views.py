from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth import logout
from userapp.models import Signup,Enrollment   

# Create your views here.
def admin_dashboard(request):
    total_courses= Course.objects.count()
    total_students = Signup.objects.count()  # count all students
    total_enrollments = Enrollment.objects.count()  # count all enrollments
    return render(request,'admin_dashboard.html',{'total_courses':total_courses,'total_students':total_students,'total_enrollments':total_enrollments})

def admin_login(request):
    if request.method=='POST':
        unm= request.POST["username"]
        pas = request.POST["password"]

        if unm=="admin" and pas=="admin@123":
            print("Login successfully!")
            return redirect("admin_dashboard")
        else:
            print("Error! Login Failed!")
    return render(request,'admin_login.html')

def admin_course_form(request):
    if request.method == "POST":
        title = request.POST.get("title")
        instructor = request.POST.get("instructor")
        category = request.POST.get("category")
        duration = request.POST.get("duration")
        fee = request.POST.get("fee")
        video_preview = request.POST.get("video_preview")
        syllabus = request.POST.get("syllabus")

        Course.objects.create(
            title=title,
            instructor=instructor,
            category=category,
            duration=duration,
            fee=fee,
            video_preview=video_preview,
            syllabus=syllabus
        )

        messages.success(request, "Course Added Successfully 🎉")
        return redirect("/adminapp/admin_course_list") 
    return render(request,'admin_course_form.html')
  # redirect to list page

def admin_course_list(request):
    courses = Course.objects.all().order_by("-id")   # latest first

    from django.shortcuts import render
from .models import Course

def admin_course_list(request):
    courses = Course.objects.all()

    # Get filter values
    search = request.GET.get('search')
    category = request.GET.get('category')
    duration = request.GET.get('duration')
    min_fee = request.GET.get('min_fee')
    max_fee = request.GET.get('max_fee')

    # Search
    if search:
        courses = courses.filter(title__icontains=search)

    # Category
    if category:
        courses = courses.filter(category__iexact=category)

    # Duration (optional contains match)
    if duration:
        courses = courses.filter(duration__icontains=duration)

    # Min Fee
    if min_fee:
        courses = courses.filter(fee__gte=min_fee)

    # Max Fee
    if max_fee:
        courses = courses.filter(fee__lte=max_fee)

    return render(request, "admin_course_list.html", {"courses": courses})



def admin_logout(request):
    logout(request)
    return redirect('admin_login')

def edit_course(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == "POST":
        course.title = request.POST.get("title")
        course.instructor = request.POST.get("instructor")
        course.category = request.POST.get("category")
        course.duration = request.POST.get("duration")
        course.fee = request.POST.get("fee")
        course.video_preview = request.POST.get("video_preview")
        course.syllabus = request.POST.get("syllabus")

        course.save()
        messages.success(request, "Course Updated Successfully ✔")
        return redirect("admin_course_list")

    return render(request, "edit_course.html", {"course": course})


def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, "Course Deleted Successfully ❌")
    return redirect("admin_course_list")

