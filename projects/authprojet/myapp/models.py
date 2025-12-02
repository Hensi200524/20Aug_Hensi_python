from django.db import models

# Create your models here.
class Userregister(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    fullname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phno = models.BigIntegerField()
    
    
