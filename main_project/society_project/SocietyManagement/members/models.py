from django.db import models
from accounts.models import Usersignup
from adminpanel.models import Competition

# Create your models here.
class Member(models.Model):
    user = models.ForeignKey(Usersignup, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    flat_no = models.CharField(max_length=20)
    contact = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)


STATUS_CHOICES = [
    ("Pending", "Pending"),
    ("In Progress", "In Progress"),
    ("Solved", "Solved"),
]

CATEGORY_CHOICES = [
    ("Water Supply", "Water Supply"),
    ("Electricity", "Electricity"),
    ("Security", "Security"),
    ("Cleaning", "Cleaning"),
    ("Parking", "Parking"),
    ("Lift Issue", "Lift Issue"),
    ("Other", "Other"),
]

class Complaint(models.Model):
    user = models.ForeignKey(Usersignup, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='complaint_images/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    admin_reply = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class CompetitionRegistration(models.Model):
    user = models.ForeignKey(Usersignup, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)
