from django.contrib import admin
from .models import Student, enroll
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'grade']

class EnrollAdmin(admin.ModelAdmin):
    list_display = ['user','get_lecture_list']

admin.site.register(Student, StudentAdmin)
admin.site.register(enroll,EnrollAdmin)