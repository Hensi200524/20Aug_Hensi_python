from django.contrib import admin
from django.urls import path,include
from adminapp import views

urlpatterns = [
    path('',views.admin_login,name='admin_login'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('admin_course_form/',views.admin_course_form,name='admin_course_form'),
    path('admin_course_list/',views.admin_course_list,name='admin_course_list'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('edit_course/<int:id>/', views.edit_course, name='edit_course'),
    path('delete_course/<int:id>/', views.delete_course, name='delete_course'),
]