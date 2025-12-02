from django.contrib import admin
from django.urls import path,include
from proapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('showdata/',views.showdata),
    path('deletedata/<int:id>',views.deletedata,name = 'deletedata')
]