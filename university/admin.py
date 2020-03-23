from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from mptt.admin import DraggableMPTTAdmin
from .models import College

class CollegeAdmin(DjangoMpttAdmin):
    pass

admin.site.register(College,CollegeAdmin)