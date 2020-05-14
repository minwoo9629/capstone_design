from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

class College(MPTTModel):
    parent = TreeForeignKey('self',verbose_name="소속" ,null=True, related_name='children', db_index=True,on_delete=models.CASCADE)
    name = models.CharField(verbose_name="이름", null=True, unique=True ,max_length=100)

    class MPTTMeta:
        order_insertion_by = ['parent']

    def __str__(self):
        return self.name


