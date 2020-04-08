from django.db import models
from django.contrib.auth.models import User
from university.models import College
# Create your models here.
class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': "professor"})
    major= models.ForeignKey(College,verbose_name="소속학과" ,on_delete=models.PROTECT, to_field="name", db_column="major", null=True)
    prof_code = models.CharField(verbose_name="교수 코드",max_length=20, unique=True)

    def __str__(self):
        return self.prof_code