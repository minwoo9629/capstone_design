from django.db import models
from django.contrib.auth.models import User,Group

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': "student"})
    major = models.CharField(max_length=30)
    grade = models.IntegerField()
