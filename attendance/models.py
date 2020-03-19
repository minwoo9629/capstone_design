from django.db import models
from django.contrib.auth.models import User,Group
from lecture.models import Lecture

# Create your models here.

class attendance(models.Model):
    ResultChoice = [('ATTEND','출석'),('LATE','지각'),('ABSENT','결석')]

    user = models.ForeignKey(User,on_delete=models.CASCADE,to_field='username', db_column="user", limit_choices_to={'groups__name': "student"})
    lecture_code = models.ForeignKey(Lecture, on_delete=models.CASCADE,to_field='lecture_code', db_column="lecture_code")
    time = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=10,choices=ResultChoice, default=True,)