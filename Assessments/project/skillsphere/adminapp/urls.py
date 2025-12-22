from django.contrib import admin
from django.urls import path
from adminapp import views
from .views import add_course

urlpatterns = [
    path('',views.index,name='index'),
    path('admin-panel/add-course/', add_course, name='add_course'),
]
