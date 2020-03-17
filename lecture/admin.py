from django.contrib import admin
from .models import Subject, LectureRoom
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_name', 'subject_code', 'split_code', 'prof_code', 'semester']

admin.site.register(Subject, SubjectAdmin)
admin.site.register(LectureRoom)
# Register your models here.
