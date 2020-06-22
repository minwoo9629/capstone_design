from django.db import models
from django.contrib.auth.models import User,Group
from lecture.models import Lecture
import jsonfield
# Create your models here.

class attendance(models.Model):
    ResultChoice = [('ATTEND','출석'),('LATE','지각'),('ABSENT','결석')]
    username = models.ForeignKey(User,on_delete=models.CASCADE,to_field='username', db_column="username", limit_choices_to={'groups__name': "student"})
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    result = jsonfield.JSONField()
    final_result = models.CharField(max_length=10, default="처리중")

class userlog(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE,to_field='username', db_column="username", limit_choices_to={'groups__name': "student"})
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    time = models.DateTimeField() #2020-06-22 13:36:12
    #time = models.CharField(max_length=20)
    check = models.CharField(verbose_name="in/out", max_length=5)
    
class facial_attendance(models.Model):
    ResultChoice = [('ATTEND','출석'),('LATE','지각'),('ABSENT','결석')]
    username = models.ForeignKey(User,on_delete=models.CASCADE,to_field='username', db_column="username", limit_choices_to={'groups__name': "student"})
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    time = models.DateField(auto_now_add=True)
    result = jsonfield.JSONField()
    final_result = models.CharField(max_length=10, default="처리중")