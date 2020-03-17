from django.contrib import admin
from .models import UserInfo
from django.contrib.auth.models import User
# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone']

admin.site.register(UserInfo,UserInfoAdmin)
