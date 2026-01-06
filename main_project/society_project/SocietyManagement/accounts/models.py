from django.db import models

# Create your models here.
class Usersignup(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.BigIntegerField()
    house = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    confirm_password = models.CharField(max_length=10)
    is_member_approved = models.BooleanField(default=False)

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)