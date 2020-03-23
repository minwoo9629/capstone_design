from django.db import models
from django.contrib.auth.models import User,Group
from university.models import College

def user_photo_path(instance, filename):
    return 'hanbat/{}/{}/{}'.format(instance.major_code,instance.grade,filename)

class Student(models.Model):
    user = models.OneToOneField(User,verbose_name="학번",on_delete=models.CASCADE, limit_choices_to={'groups__name': "student"})
    major_choice = College.objects.filter(level__exact=1)
    print(major_choice)
    major= models.ForeignKey(College, on_delete=models.PROTECT, to_field="name", db_column="major", null=True)
    grade = models.IntegerField(verbose_name="학년")
    photo = models.ImageField(verbose_name="사진",null=True, upload_to=user_photo_path)


class enroll(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,to_field='username', db_column="user")