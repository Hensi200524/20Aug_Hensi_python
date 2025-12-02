from django.db import models

# Create your models here.
class contactinfo(models.Model):
    fullname = models.CharField(max_length=20)
    email = models.EmailField()
    phno = models.BigIntegerField()
    msg = models.TextField(max_length=200)
