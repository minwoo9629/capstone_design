from django.contrib import admin
from .models import Lecture, Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_code', 'building', 'room_number']

class LectureAdmin(admin.ModelAdmin):
    list_display = ['name','lecture_code','prof_code','split_code','room_code', 'semester']


admin.site.register(Room, RoomAdmin)
admin.site.register(Lecture, LectureAdmin)
# Register your models here.
