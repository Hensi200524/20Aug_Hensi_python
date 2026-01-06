from django.urls import path
from . import views

urlpatterns = [
    path("member/member_dashboard/", views.member_dashboard, name="member_dashboard"),
    path("member/member_complaints/",views.member_complaints,name='member_complaints'),
    path("member/add_complaint/",views.add_complaint,name="add_complaint"),
    path("member/member_maintenance/",views.member_maintenance,name='member_maintenance'),
    path('member/pay_maintenance/<int:id>/', views.pay_maintenance, name='pay_maintenance'),
    path("events/", views.member_events, name="member_events"),
    path("competitions/", views.member_competitions, name="member_competitions"),
    path("competitions/register/<int:competition_id>/",views.competition_register,name="competition_register"),
    path("gallery/", views.member_gallery, name="member_gallery"),
    path("emergency/", views.member_emergency, name="member_emergency"),
]