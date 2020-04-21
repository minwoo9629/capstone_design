from django.db import models
from django.contrib.auth.models import User,Group
from lecture.models import Lecture
from university.models import College
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage


class OverwriteStorage(FileSystemStorage):
    # 같은 이름의 file이 존재하는 경우 overwirte.
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name
    
    # Media file의 경로 지정
def user_photo_path(instance, filename):
    # 사용자가 업로드 하는 파일의 이름을 해당 유저의 username(학번).jpg로 저장하도록 함.
    filename = str(instance.username) + ".jpg"
    return 'hanbat/{}/{}/{}'.format(instance.major,instance.grade,filename)

class Student(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [ ('FRESHMAN', '1'),('SOPHOMORE', '2'),('JUNIOR', '3'),('SENIOR', '4')]
    username = models.OneToOneField(User,verbose_name="학번",on_delete=models.CASCADE, to_field='username', db_column="username", unique=True, limit_choices_to={'groups__name': "student"})
    major= models.ForeignKey(College,verbose_name="학과" ,on_delete=models.PROTECT, to_field="name", db_column="major", null=True, limit_choices_to={'level':1})
    grade = models.CharField(verbose_name="학년", max_length=10, choices=YEAR_IN_SCHOOL_CHOICES)
    photo = models.ImageField(verbose_name="사진",null=True, upload_to=user_photo_path, storage=OverwriteStorage())
    take_lectures = models.ManyToManyField(Lecture, verbose_name="수강 강의", through='TakeLectures', through_fields=('username','lectures'))

    def __str__(self):

        user = User.objects.get(username=self.username)
        first_name = user.first_name
        last_name = user.last_name
        return str(self.username) + "(" + last_name + first_name + ")"

class TakeLectures(models.Model):
    username = models.ForeignKey(Student,verbose_name="학번",on_delete=models.CASCADE, to_field='username', db_column="username")
    lectures = models.ForeignKey(Lecture, verbose_name="수강 강의",on_delete=models.CASCADE)

