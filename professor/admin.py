from django.contrib import admin
from .models import Professor

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['username','major']

admin.site.register(Professor, ProfessorAdmin)