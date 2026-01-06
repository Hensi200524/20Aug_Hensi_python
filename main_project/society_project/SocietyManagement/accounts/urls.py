from django.contrib import admin
from django.urls import path,include
from accounts import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),  
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
]
