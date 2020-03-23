from django.db import models
from professor.models import Professor
# Create your models here.
class Room(models.Model):
    room_code = models.CharField(verbose_name="강의실 코드",max_length=20, unique=True)
    building = models.CharField(verbose_name="동",max_length=20)
    room_number = models.CharField(verbose_name="호수",max_length=20)

    def __str__(self):
        return self.room_code

class Lecture(models.Model):
    name = models.CharField(verbose_name="강의명",max_length=30)
    lecture_code = models.CharField(verbose_name="강의 코드",max_length=20, unique=True)
    prof_code = models.ForeignKey(Professor,on_delete=models.CASCADE,to_field='prof_code', db_column="prof_code")
    split_code = models.CharField(verbose_name="분반 코드",max_length=10)
    room_code = models.ForeignKey(Room, on_delete=models.CASCADE, to_field='room_code', db_column="room_code")
    semester = models.IntegerField(verbose_name="학기")

    def __str__(self):
        return self.name

class Beacon(models.Model):
    room_code = models.OneToOneField(Room, on_delete=models.CASCADE, to_field='room_code', db_column="room_code")
    beacon_uuid = models.CharField(max_length=30)
    beacon_major = models.CharField(max_length=30)
    beacon_minor = models.CharField(max_length=30)