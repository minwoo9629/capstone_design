from django.db import models
from django.contrib.auth.models import User,Group
from lecture.models import Lecture
from university.models import College
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage


class OverwriteStorage(FileSystemStorage):
    # 같은 이름의 file이 존재하는 경우 overwirte
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name
def user_photo_path(instance, filename):
    filename = str(instance.user) + ".jpg"
    return 'hanbat/{}/{}/{}'.format(instance.major,instance.grade,filename)

class Student(models.Model):
    user = models.OneToOneField(User,verbose_name="학번",on_delete=models.CASCADE, limit_choices_to={'groups__name': "student"})
    major= models.ForeignKey(College,verbose_name="학과" ,on_delete=models.PROTECT, to_field="name", db_column="major", null=True, limit_choices_to={'level':1})
    grade = models.IntegerField(verbose_name="학년")
    photo = models.ImageField(verbose_name="사진",null=True, upload_to=user_photo_path, storage=OverwriteStorage())


class enroll(models.Model):
    user = models.ForeignKey(User,verbose_name="학번",on_delete=models.CASCADE,to_field='username', db_column="user",limit_choices_to={'groups__name': "student"})
    lecture_list = models.ManyToManyField(Lecture, verbose_name="수강 강의")

    def get_lecture_list(self):
        return ",".join([str(l) for l in self.lecture_list.all()])
