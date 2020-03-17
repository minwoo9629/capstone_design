from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': "professor"})
    major = models.CharField(max_length=30)
    prof_code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.prof_code