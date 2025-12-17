from django.contrib import admin
from django.urls import path,include
from adminapp import views

urlpatterns = [
    path('',views.admin_login,name='admin_login'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('admin_manage_users/',views.admin_manage_users,name='admin_manage_users'),
    path('admin_manage_notes/',views.admin_manage_notes,name='admin_manage_notes'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('admin_user_delete/<int:uid>',views.admin_user_delete,name='admin_user_delete'),
    path('approve_note/<int:id>',views.approve_note,name='approve_note'),
    path('reject_note/<int:id>',views.reject_note,name='reject_note'),
    path('admin_show_contact/',views.admin_show_contact,name='admin_show_contact'),
    path('admin_contact_delete/<int:cid>',views.admin_contact_delete,name='admin_contact_delete'),
    path('admin_user_view/<int:id>',views.admin_user_view,name='admin_user_view'),
    path('admin_manage_notes_cards',views.admin_manage_notes_cards,name='admin_manage_notes_cards'),
]
