from django.db import models
from professor.models import Professor
# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=30)
    subject_code = models.CharField(max_length=20)
    split_code = models.CharField(max_length=10)
    prof_code = models.ForeignKey(Professor,on_delete=models.CASCADE,to_field='prof_code', db_column="prof_code")
    semester = models.IntegerField()

class LectureRoom(models.Model):
    lecture_room_name = models.CharField(max_length=20)
    lecture_room_code = models.CharField(max_length=20)
    beacon_uuid = models.CharField(max_length=30)
    beacon_major = models.CharField(max_length=30)
    beacon_minor = models.CharField(max_length=30)