from django.contrib import admin
from .models import attendance, userlog, facial_attendance
# Register your models here.

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['username', 'lecture', 'time', 'result', 'final_result']

class UserLogAdmin(admin.ModelAdmin):
    list_display = ['username', 'lecture', 'time','check']

class FacialAttendanceAdmin(admin.ModelAdmin):
    list_display = ['username', 'lecture', 'time', 'result', 'final_result']
admin.site.register(attendance, AttendanceAdmin)
admin.site.register(userlog,UserLogAdmin)
admin.site.register(facial_attendance, FacialAttendanceAdmin)
