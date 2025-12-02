from django.contrib import admin
from .models import *

# Register your models here.
class contactdata(admin.ModelAdmin):
    list_display = ['id','name','email','message']

admin.site.register(contactinfo,contactdata)

