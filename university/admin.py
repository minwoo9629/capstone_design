from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from mptt.admin import DraggableMPTTAdmin
from .models import College

class CollegeAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'parent', 'name')

admin.site.register(College,CollegeAdmin)