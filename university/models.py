# -*- coding: utf-8 -*- 
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class College(MPTTModel):
    parent = TreeForeignKey('self',verbose_name="소속" ,null=True, blank= True, related_name='children', db_index=True,on_delete=models.CASCADE)
    name = models.CharField(verbose_name="이름", null=True, unique=True ,max_length=100)
    uuid = models.CharField(verbose_name="학교 구분을 위한 uuid", null=True, blank= True, unique=True, max_length=50)

    class MPTTMeta:
        order_insertion_by = ['parent']

    def __str__(self):
        return self.name


