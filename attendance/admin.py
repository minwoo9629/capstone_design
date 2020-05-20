from django.contrib import admin
from .models import attendance
# Register your models here.

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['username', 'lecture', 'time', 'result']

admin.site.register(attendance, AttendanceAdmin)
