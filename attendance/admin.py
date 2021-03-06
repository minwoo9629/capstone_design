from django.contrib import admin
from .models import Attendance, facial_attendance, userlog
# Register your models here.

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['username', 'lecture', 'time', 'result', 'final_result']

class FacialAttendanceAdmin(admin.ModelAdmin):
    list_display = ['username', 'lecture', 'time', 'result', 'final_result']

class UserLogAdmin(admin.ModelAdmin):
    list_display = ['username', 'lecture', 'time','check']
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(facial_attendance, FacialAttendanceAdmin)
admin.site.register(userlog,UserLogAdmin)
