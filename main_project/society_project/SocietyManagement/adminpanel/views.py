from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import logout
from adminpanel.models import MemberApproval
from members.models import Member
from accounts.models import Usersignup
from members.models import Complaint
from django.contrib import messages
from .models import Maintenance
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from .models import Event
from .models import Competition
from members.models import CompetitionRegistration
from .models import EmergencyContact



# ---------------- ADMIN DASHBOARD ----------------
def admin_dashboard(request):
    total_members = Usersignup.objects.count()
    pending_users = MemberApproval.objects.filter(status="pending")

    return render(request, 'admin_dashboard.html', {
        'total_members': total_members,
        'pending_users': pending_users
    })

def members_list(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "pending":
        users = Usersignup.objects.filter(memberapproval__status="pending")

    elif filter_type == "approved":
        users = Usersignup.objects.filter(memberapproval__status="Approved")

    elif filter_type == "rejected":
        users = Usersignup.objects.filter(memberapproval__status="Rejected")

    else:
        users = Usersignup.objects.all()

    return render(request, "members_list.html", {
        "users": users,
        "filter": filter_type
    })



# APPROVE USER
def approve_user(request, id):
    user = Usersignup.objects.get(id=id)
    user.is_member_approved = True
    user.save()

    # Create Member table entry
    Member.objects.get_or_create(
        user=user,
        name=user.username,
        flat_no=user.house,
        contact=user.phone,
        email=user.email
    )

    # Update approval status
    MemberApproval.objects.filter(user=user).update(status="Approved")

    # ---------- SEND APPROVAL EMAIL ----------
    subject = "✅ SocietyHub Approval Successful"

    html_content = render_to_string("emails/member_approved.html", {
        "username": user.username
    })

    email = EmailMultiAlternatives(
        subject=subject,
        body="Your SocietyHub account has been approved.",
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email]
    )

    email.attach_alternative(html_content, "text/html")
    email.send()

    return redirect("members_list")

# REJECT USER
def reject_user(request, id):
    user = Usersignup.objects.get(id=id)
    user.is_member_approved = False
    user.save()

    Member.objects.filter(user=user).delete()

    MemberApproval.objects.filter(user=user).update(status="Rejected")

    # ---------- SEND REJECTION EMAIL ----------
    subject = "⏳ SocietyHub Approval Pending"

    html_content = render_to_string("emails/member_rejected.html", {
        "username": user.username
    })

    email = EmailMultiAlternatives(
        subject=subject,
        body="Your SocietyHub account is not approved yet.",
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email]
    )

    email.attach_alternative(html_content, "text/html")
    email.send()

    return redirect("members_list")

# DELETE
def delete_member(request, id):
    user = get_object_or_404(Usersignup, id=id)

    # delete member if exists
    Member.objects.filter(user=user).delete()

    # delete user
    user.delete()

    return redirect("members_list")

def edit_member(request, id):
    user = get_object_or_404(Usersignup, id=id)

    if request.method == "POST":
        user.email = request.POST.get("email")
        user.phone = request.POST.get("phone")
        user.house = request.POST.get("house")
        user.save()

        # update member table also
        Member.objects.filter(user=user).update(
            name=user.username,
            flat_no=user.house,
            contact=user.phone,
            email=user.email
        )

        return redirect("members_list")

    return render(request, "edit_member.html", {"user": user})


# ---------------- LOGOUT ----------------
def adminlogout(request):
    logout(request)
    return redirect('login')

def admin_complaints(request):
    complaints = Complaint.objects.all().order_by('-created_at')
    return render(request, 'admin_complaints.html', {'complaints': complaints})

def update_complaint(request, id):
    complaint = Complaint.objects.get(id=id)

    if request.method == 'POST':
        complaint.status = request.POST.get('status')
        complaint.admin_reply = request.POST.get('admin_reply')
        complaint.save()
        messages.success(request, 'Complaint updated successfully!')
        return redirect('admin_complaints')

    return render(request, 'update_complaint.html', {'complaint': complaint})

def delete_complaint(request, id):
    complaint = Complaint.objects.get(id=id)
    complaint.delete()
    messages.success(request, "Complaint deleted successfully")
    return redirect("admin_complaints")

def admin_maintenance_list(request):
    maintenances = Maintenance.objects.all().order_by("-id")
    return render(request,"admin_maintenance_list.html",{"maintenances": maintenances})

def add_maintenance(request):
    approved_members = Usersignup.objects.filter(memberapproval__status="Approved")

    if request.method == "POST":
        user_id = request.POST.get("member")
        user = Usersignup.objects.get(id=user_id)

        maintenance = Maintenance.objects.create(
            user=user,
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            month=request.POST.get("month"),
            year=request.POST.get("year"),
            amount=request.POST.get("amount"),
            status="Pending"
        )

        # -------- Beautiful Email Template --------
        subject = "⚠ Maintenance Pending - SocietyHub"

        html_content = render_to_string("emails/maintenance_pending.html", {
            "username": user.username,
            "amount": maintenance.amount,
            "month": maintenance.month,
            "year": maintenance.year,
        })

        email = EmailMultiAlternatives(
            subject=subject,
            body="Maintenance Pending Notification",
            from_email=settings.EMAIL_HOST_USER,
            to=[user.email]
        )

        email.attach_alternative(html_content, "text/html")
        email.send()

        return redirect("admin_maintenance_list")

    return render(request, "add_maintenance.html", {"approved_members": approved_members})

def update_maintenance(request,id):
    maintenance = get_object_or_404(Maintenance, id=id)

    if request.method == "POST":
        maintenance.status = request.POST.get("status")
        maintenance.save()
        return redirect("admin_maintenance_list")
    return render(request,"update_maintenance.html",{"maintenance": maintenance})

def delete_maintenance(request, id):
    maintenance = get_object_or_404(Maintenance, id=id)
    maintenance.delete()
    return redirect("admin_maintenance_list")

def admin_events_list(request):
    events = Event.objects.all().order_by("-created_at")
    return render(request, "admin_events_list.html", {"events": events})


def add_event(request):
    if request.method == "POST":
        title = request.POST.get("title")
        event_date = request.POST.get("event_date")
        event_time = request.POST.get("event_time")
        location = request.POST.get("location")
        description = request.POST.get("description")

        Event.objects.create(
            title=title,
            event_date=event_date,
            event_time=event_time,
            location=location,
            description=description
        )

        messages.success(request, "Event Added Successfully 🎉")
        return redirect("admin_events_list")

    return render(request, "add_event.html")

def update_event(request, id):
    event = get_object_or_404(Event, id=id)

    if request.method == "POST":
        event.title = request.POST.get("title")
        event.event_date = request.POST.get("event_date")
        event.event_time = request.POST.get("event_time")
        event.location = request.POST.get("location")
        event.description = request.POST.get("description")
        event.save()

        messages.success(request, "Event Updated Successfully!")
        return redirect("admin_events_list")

    return render(request, "update_event.html", {"event": event})


def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    event.delete()
    messages.success(request, "Event Deleted Successfully!")
    return redirect("admin_events_list")

def admin_competition_list(request):
    competitions = Competition.objects.all().order_by('-date')
    return render(request, 'admin_competition_list.html', { 'competitions': competitions})

def add_competition(request):
    if request.method == 'POST':
        Competition.objects.create(
            title=request.POST.get('title'),
            date=request.POST.get('date'),
            time=request.POST.get('time'),
            location=request.POST.get('location'),
            description=request.POST.get('description'),
        )
        return redirect('admin_competition_list')

    return render(request, 'add_competition.html')

def update_competition(request, id):
    competition = get_object_or_404(Competition, id=id)

    if request.method == 'POST':
        competition.title = request.POST.get('title')
        competition.date = request.POST.get('date')
        competition.time = request.POST.get('time')
        competition.location = request.POST.get('location')
        competition.description = request.POST.get('description')
        competition.save()

        return redirect('admin_competition_list')

    return render(request, 'update_competition.html', {'competition': competition})

def delete_competition(request, id):
    competition = get_object_or_404(Competition, id=id)
    competition.delete()
    return redirect('admin_competition_list')

def admin_competition_registrations(request, comp_id):
    competition = get_object_or_404(Competition, id=comp_id)

    registrations = CompetitionRegistration.objects.filter(
        competition=competition
    ).select_related("user")

    return render(request, "admin_competition_registrations.html", {
        "competition": competition,
        "registrations": registrations
    })

def admin_emergency_list(request):
    contacts = EmergencyContact.objects.all().order_by("-id")
    return render(request, "admin_emergency_list.html", {
        "contacts": contacts
    })


def add_emergency(request):
    if request.method == "POST":
        EmergencyContact.objects.create(
            title=request.POST.get("title"),
            phone=request.POST.get("phone"),
            description=request.POST.get("description")
        )
        return redirect("admin_emergency_list")

    return render(request, "add_emergency.html")


def delete_emergency(request, id):
    contact = get_object_or_404(EmergencyContact, id=id)
    contact.delete()
    return redirect("admin_emergency_list")


