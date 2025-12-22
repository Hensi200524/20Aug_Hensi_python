from django.contrib import admin
from django.urls import path
from userapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('courses/',views.courses,name='courses'),
    path('course_detail/',views.course_detail,name='course_detail'),
    path('my_courses/',views.my_courses,name='my_courses'),
    path('profile/',views.profile,name='profile'),
]
