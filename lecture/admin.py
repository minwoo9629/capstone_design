from django.contrib import admin
from .models import Lecture, Room, Beacon

class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_code', 'building', 'room_number']

class LectureAdmin(admin.ModelAdmin):
    list_display = ['name','lecture_code','prof_code','split_code','room_code', 'semester']

class BeaconAdmin(admin.ModelAdmin):
    list_display = ['room_code','beacon_major','beacon_minor']

admin.site.register(Room, RoomAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Beacon, BeaconAdmin)
# Register your models here.
