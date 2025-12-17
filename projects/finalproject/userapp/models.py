from django.db import models

# Create your models here.
class Usersignup(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    cpassword = models.CharField(max_length=20)

class Notesdata(models.Model):
    submitted_at=models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Usersignup,on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    file=models.FileField(upload_to='NotesData')
    desc=models.TextField()
    status_choice=[
        ('Pending','Pending'),
        ('Approve','Approve'),
        ('Reject','Reject')
    ]
    status=models.TextField(choices=status_choice)
    updated_at=models.DateTimeField(blank=True,null=True)

class Usercontact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
