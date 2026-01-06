from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.getall),
    path('getsid/<int:id>/',views.getsid),
    path('deletesid/<int:id>',views.deletesid),
    path('savedata/',views.savedata),
    path('updatedata/<int:id>',views.updatedata),
]