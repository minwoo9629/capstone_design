# Generated by Django 2.0.13 on 2020-03-22 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_student_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.IntegerField(verbose_name='학년'),
        ),
        migrations.AlterField(
            model_name='student',
            name='major_code',
            field=models.CharField(max_length=30, verbose_name='학과'),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(null=True, upload_to=student.models.user_photo_path, verbose_name='사진'),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(limit_choices_to={'groups__name': 'student'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='학번'),
        ),
    ]