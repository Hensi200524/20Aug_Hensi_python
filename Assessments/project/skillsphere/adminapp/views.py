from django.shortcuts import render,redirect
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CourseForm

# Create your views here.
def index(request):
    return render(request,'index.html')

@staff_member_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')  # Successful save → Courses list page
    else:
        form = CourseForm()  # GET → empty form
        return render(request, 'adminapp/add_course.html', {'form': form})

