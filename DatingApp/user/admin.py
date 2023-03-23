from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.auth.forms import UserCreationForm
# Register your models here.


class UserAdmin(BaseUserAdmin):
    model = User
    fieldsets = BaseUserAdmin.fieldsets +(
        ('Detail' ,{'fields':('dob','country','city','gender','interest',)}),)
    list_display = ['username','email']
    search_fields =['email','username']
    ordering =('email',)


admin.site.register(User,UserAdmin)
    

    