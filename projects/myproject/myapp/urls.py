from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('service/',views.service),
    path('team/',views.team),
    path('testimonial/',views.testimonial),
    path('showdata/',views.showdata),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
]
