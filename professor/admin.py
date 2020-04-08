from django.contrib import admin
from .models import Professor
# Register your models here.
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['user', 'major', 'prof_code']

admin.site.register(Professor, ProfessorAdmin)