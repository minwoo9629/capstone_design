from django.db import models
from django.contrib.auth.models import User, Group
from university.models import College
# Create your models here.
class Professor(models.Model):
    # User Model 중 group이 professor인 User만
    username = models.OneToOneField(User, on_delete=models.CASCADE, to_field='username', db_column="username", unique=True, limit_choices_to={'groups__name': "professor"})
    major = models.ForeignKey(College,verbose_name="소속학과" ,on_delete=models.PROTECT, to_field="name", db_column="major", null=True)
    code = models.CharField(verbose_name="교수 코드",max_length=20, null=True, unique=True)

    def __str__(self):
        user = User.objects.get(username=self.username)
        first_name = user.first_name
        last_name = user.last_name
        return last_name + first_name + "(" + str(self.major) + ")"