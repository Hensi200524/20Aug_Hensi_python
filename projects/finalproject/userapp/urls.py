from django.contrib import admin
from django.urls import path,include
from userapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('notes/',views.notes,name='notes'),
    path('profile/',views.profile,name='profile'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('otpverify/',views.otpverify,name='otpverify'),
    path('userlogout/',views.userlogout,name='userlogout'),
]