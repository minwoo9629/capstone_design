from django.contrib import admin
from .models import Student, TakeLectures
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['grade', 'username', 'photo']

class TakeLecturesAdmin(admin.ModelAdmin):
    list_display = ['lectures','username']

admin.site.register(Student, StudentAdmin)
admin.site.register(TakeLectures,TakeLecturesAdmin)
=======
    list_display = ['username', 'grade']

class TakeLecturesAdmin(admin.ModelAdmin):
    list_display = ['username', 'lectures']

admin.site.register(Student, StudentAdmin)
admin.site.register(TakeLectures, TakeLecturesAdmin)
>>>>>>> d152129f14e52b9f39da01d2821a757358faa7e7
