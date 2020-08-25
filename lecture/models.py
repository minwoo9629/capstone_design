# -*- coding: utf-8 -*- 
from django.db import models
import jsonfield
from professor.models import Professor
from university.models import College
# Create your models here.
class Room(models.Model):
    code = models.CharField(verbose_name="강의실 코드",max_length=20, unique=True)
    building = models.CharField(verbose_name="동",max_length=20)
    number = models.CharField(verbose_name="호수",max_length=20)
    camera = models.GenericIPAddressField(max_length=64, verbose_name="ip카메라", null=True)

    def __str__(self):
        return self.code

class Lecture(models.Model):
    SEMESTER_CHOICES = [('1st_semester','1'),('Seconde_semester','2')]
    TERM_CHOICES = [('15','15'),('30','30'),('45','45'),('60','60')]
    name = models.CharField(verbose_name="강의명",max_length=30)
    code = models.CharField(verbose_name="강의 코드",max_length=20)
    professor = models.ManyToManyField(Professor, verbose_name="교수", through='GiveLectures')
    split_code = models.CharField(verbose_name="분반 코드",max_length=3, unique=True)
    room_code = models.ForeignKey(Room, on_delete=models.CASCADE, to_field='code', db_column="room_code")
    semester = models.CharField(verbose_name="학기",max_length=20, choices=SEMESTER_CHOICES)
    day_of_the_week = models.CharField(verbose_name="수업 요일", max_length=10, null=True)
    start_time = models.TimeField(verbose_name="수업 시작 시간",auto_now=False, auto_now_add=False,default="00:00")
    end_time = models.TimeField(verbose_name="수업 종료 시간",auto_now=False, auto_now_add=False, default="00:00")
    term = models.CharField(verbose_name="출석 반복 시간", max_length=5, choices=TERM_CHOICES, default="30")
    count = models.IntegerField(verbose_name="반복 횟수", null=True)

class GiveLectures(models.Model):
    username = models.ForeignKey(Professor,verbose_name="교수",on_delete=models.CASCADE, to_field='username', db_column="username")
    lectures = models.ForeignKey(Lecture, verbose_name="담당 강의",on_delete=models.CASCADE)


class Beacon(models.Model):
    room_code = models.OneToOneField(Room, verbose_name="강의실 코드", on_delete=models.CASCADE, to_field='code', db_column="room_code")
    uuid = models.ForeignKey(College,verbose_name="학교와 대응되는 비콘 UUID 값", on_delete=models.SET_NULL, to_field="uuid", db_column="uuid", null=True, max_length=50, limit_choices_to={'level':0})
    major = models.CharField(verbose_name="비콘 major 값",max_length=10)
    minor = models.CharField(verbose_name="비콘 minor 값",max_length=10)