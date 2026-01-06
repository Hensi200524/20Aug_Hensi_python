from django.db import models
from accounts.models import Usersignup

# Create your models here.
class MemberApproval(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    )

    user = models.OneToOneField(Usersignup, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

class Maintenance(models.Model):
    user = models.ForeignKey(Usersignup, on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField(max_length=150)
    description = models.TextField()

    month = models.CharField(max_length=20)
    year = models.IntegerField()

    amount = models.IntegerField()

    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Paid", "Paid"),
        ("Overdue", "Overdue"),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")

    created_at = models.DateTimeField(auto_now_add=True)


class Event(models.Model):
    title = models.CharField(max_length=200)
    event_date = models.DateField()
    event_time = models.TimeField()
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Competition(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class EmergencyContact(models.Model):
    title = models.CharField(max_length=100)   # Police, Ambulance
    phone = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

