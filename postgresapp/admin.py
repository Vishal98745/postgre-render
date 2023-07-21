from django.contrib import admin

from .models import *
admin.site.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password','phone']


