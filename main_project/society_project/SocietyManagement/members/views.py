from django.shortcuts import render, redirect,get_object_or_404
from .models import Complaint
from .forms import ComplaintForm
from django.contrib import messages
from adminpanel.models import Maintenance
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from adminpanel.models import Event, Competition
from .models import CompetitionRegistration
from .models import Usersignup
from adminpanel.models import EmergencyContact


def member_dashboard(request):
    username = request.session.get('username')

    if not username:
        return redirect("login")

    return render(request, "member_dashboard.html", {"username": username})

def member_complaints(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    complaints = Complaint.objects.filter(user_id=user_id).order_by('-created_at')
    return render(request, 'member_complaints.html', {"complaints": complaints})

def add_complaint(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    if request.method == "POST":
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user_id = user_id
            complaint.save()
            messages.success(request, "Complaint submitted successfully!")
            return redirect('member_complaints')
    else:
        form = ComplaintForm()
    
    return render(request, 'add_complaint.html', {"form": form})

def member_maintenance(request):

    # ✔ Session user id through
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('login')

    # ✔ Maintenance fetch in  session user id 
    maintenance = Maintenance.objects.filter(user_id=user_id).order_by('-id')

    return render(request, 'member_maintenance.html', {
        "maintenance": maintenance
    })

def pay_maintenance(request, id):
    maintenance = get_object_or_404(Maintenance, id=id)

    if request.method == "POST":
        maintenance.status = "Paid"
        maintenance.save()

        # ========== SEND HTML EMAIL ==========
        html_content = render_to_string("emails/maintenance_success.html", {
            "username": maintenance.user.username,
            "amount": maintenance.amount,
            "month": maintenance.month,
            "year": maintenance.year
        })

        email = EmailMultiAlternatives(
            subject="Payment Successful - SocietyHub",
            body="Maintenance Paid Successfully",
            from_email=settings.EMAIL_HOST_USER,
            to=[maintenance.user.email]
        )

        email.attach_alternative(html_content, "text/html")
        email.send()

        messages.success(request, "Maintenance Paid & Email Sent Successfully!")
        return redirect("member_maintenance")

    return render(request, "pay_maintenance.html", {"maintenance": maintenance})

def member_events(request):
    events = Event.objects.all().order_by('event_date')
    return render(request, "member_events.html", {"events": events})

def member_competitions(request):
    competitions = Competition.objects.all().order_by('date')
    return render(request, "member_competitions.html", {"competitions": competitions})

def competition_register(request, competition_id):
    competition = get_object_or_404(Competition, id=competition_id)

    if request.method == "POST":
        # later we will save registration
        return redirect("member_competitions")

    return render(
        request,
        "competition_register.html",
        {"competition": competition}
    )

def competition_register(request, comp_id):
    # ✔ Session user id fetch
    user_id = request.session.get('user_id')
    if not user_id:
        # member login na hoi to dashboard nav javu
        return redirect('member_dashboard')

    user = get_object_or_404(Usersignup, id=user_id)
    competition = get_object_or_404(Competition, id=comp_id)

    # ✔ Prevent duplicate registration
    already_registered = CompetitionRegistration.objects.filter(
        user=user,
        competition=competition
    ).exists()

    if not already_registered:
        CompetitionRegistration.objects.create(
            user=user,
            competition=competition
        )

    # ✔ After registration redirect to member dashboard
    return redirect('member_dashboard')

def member_gallery(request):
    return render(request, "member_gallery.html")

def member_emergency(request):
    contacts = EmergencyContact.objects.all()
    return render(request, "member_emergency.html", {
        "contacts": contacts
    })