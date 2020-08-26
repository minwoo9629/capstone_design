# Generated by Django 2.0.13 on 2020-04-04 08:22

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20200324_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(null=True, storage=student.models.OverwriteStorage(), upload_to=student.models.user_photo_path, verbose_name='사진'),
        ),
    ]