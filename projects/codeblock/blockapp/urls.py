from django.contrib import admin
from django.urls import path,include
from blockapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
]
