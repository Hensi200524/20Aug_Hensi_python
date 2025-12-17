from django.db import models

# Create your models here.
class UserAccount(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
