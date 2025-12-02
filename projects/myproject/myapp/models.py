from django.db import models

# Create your models here.
class contactinfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=500)
