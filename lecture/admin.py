from django.contrib import admin
from .models import Lecture, Room, Beacon, GiveLectures

class RoomAdmin(admin.ModelAdmin):
    list_display = ['code', 'building', 'number']

class LectureAdmin(admin.ModelAdmin):
    list_display = ['name','code', 'split_code','room_code', 'semester','day_of_the_week','start_time','end_time', 'term', 'count']

class BeaconAdmin(admin.ModelAdmin):
    list_display = ['room_code','major','minor']

class GiveLecturesAdmin(admin.ModelAdmin):
    list_display = ['username', 'lectures']    

admin.site.register(Room, RoomAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Beacon, BeaconAdmin)
admin.site.register(GiveLectures, GiveLecturesAdmin)
# Register your models here.
