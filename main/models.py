from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, to_field='username', db_column="username")
    phone = models.CharField(max_length=20)