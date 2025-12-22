from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    instructor = models.CharField(max_length=100)
    description = models.TextField()
    fees = models.IntegerField()
    duration = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
