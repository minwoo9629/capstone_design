from django.contrib import admin
from .models import attendance, userlog
# Register your models here.

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['username', 'lecture', 'time', 'result', 'final_result']

class UserLogAdmin(admin.ModelAdmin):
    list_display = ['username', 'lecture', 'time','check']

admin.site.register(attendance, AttendanceAdmin)
admin.site.register(userlog,UserLogAdmin)
