from django.db import models
# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    instructor = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    video_preview = models.URLField(max_length=500, blank=True, null=True)
    syllabus = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

