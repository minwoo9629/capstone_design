from django.db import models
import jsonfield
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
    day_of_the_week = models.CharField(verbose_name="수업 요일", max_length=10, null=True)
    start_time = models.TimeField(verbose_name="수업 시작 시간",auto_now=False, auto_now_add=False, default="00:00")
    end_time = models.TimeField(verbose_name="수업 종료 시간",auto_now=False, auto_now_add=False, default="00:00")


    def __str__(self):
        return self.name

class Beacon(models.Model):
    room_code = models.OneToOneField(Room, on_delete=models.CASCADE, to_field='room_code', db_column="room_code")
    beacon_major = models.CharField(max_length=30)
    beacon_minor = models.CharField(max_length=30)