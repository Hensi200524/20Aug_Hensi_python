from django.contrib import admin
from django.urls import path,include
from userapp import views

urlpatterns = [

    path('', views.home, name="home"),
    path('courses/', views.courses, name="courses"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('course_detail/<int:id>/',views.course_detail,name='course_detail'), 
    path('enroll_course/<int:id>/', views.enroll_course, name='enroll_course'),
    path('my_courses/', views.my_courses, name='my_courses'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path("user_profile/", views.user_profile, name="user_profile"),
    path('payment/<int:id>/', views.payment, name="payment"),
    path('payment-success/<int:id>/', views.payment_success, name="payment_success"),
    path("student_dashboard",views.student_dashboard, name="student_dashboard"),
    path('password_reset/', views.password_reset, name='password_reset'),  
]