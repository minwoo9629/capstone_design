from django.db import models
import jsonfield
from professor.models import Professor
# Create your models here.
class Room(models.Model):
    code = models.CharField(verbose_name="강의실 코드",max_length=20, unique=True)
    building = models.CharField(verbose_name="동",max_length=20)
    number = models.CharField(verbose_name="호수",max_length=20)

    def __str__(self):
        return self.code

class Lecture(models.Model):
    SEMESTER_CHOICES = [('1st_semester','1'),('Seconde_semester','2')]
    name = models.CharField(verbose_name="강의명",max_length=30)
    code = models.CharField(verbose_name="강의 코드",max_length=20)
    professor = models.ManyToManyField(Professor, verbose_name="교수", through='GiveLectures')
    split_code = models.CharField(verbose_name="분반 코드",max_length=3, unique=True)
    room_code = models.ForeignKey(Room, on_delete=models.CASCADE, to_field='code', db_column="room_code")
    semester = models.CharField(verbose_name="학기",max_length=20, choices=SEMESTER_CHOICES)
    day_of_the_week = models.CharField(verbose_name="수업 요일", max_length=10, null=True)
    start_time = models.TimeField(verbose_name="수업 시작 시간",auto_now=False, auto_now_add=False,default="00:00")
    end_time = models.TimeField(verbose_name="수업 종료 시간",auto_now=False, auto_now_add=False, default="00:00")
    

    def __str__(self):
        return self.name

class GiveLectures(models.Model):
    username = models.ForeignKey(Professor,verbose_name="교수",on_delete=models.CASCADE, to_field='username', db_column="username")
    lectures = models.ForeignKey(Lecture, verbose_name="담당 강의",on_delete=models.CASCADE)


class Beacon(models.Model):
    room_code = models.OneToOneField(Room, verbose_name="강의실 코드", on_delete=models.CASCADE, to_field='code', db_column="room_code")
    uuid = models.CharField(verbose_name="비콘 UUID 값", max_length=50, null=True, default="-")
    major = models.CharField(verbose_name="비콘 major 값",max_length=10)
    minor = models.CharField(verbose_name="비콘 minor 값",max_length=10)