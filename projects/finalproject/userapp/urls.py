from django.contrib import admin
from django.urls import path,include
from userapp import views

urlpatterns = [
    path('',views.index),
]