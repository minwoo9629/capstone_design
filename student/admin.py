from django.contrib import admin
from .models import Student, TakeLectures
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['grade']

class TakeLecturesAdmin(admin.ModelAdmin):
    list_display = ['lectures']

admin.site.register(Student, StudentAdmin)
admin.site.register(TakeLectures,TakeLecturesAdmin)