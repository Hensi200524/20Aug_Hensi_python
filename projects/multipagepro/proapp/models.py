from django.db import models

# Create your models here.
class contactinfo(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phnno = models.BigIntegerField()
    city = models.CharField(max_length=500)
    state = models.CharField(max_length=30)
    zcode = models.BigIntegerField()
    addr = models.TextField(max_length=500)
    msg = models.TextField(max_length=500)

