# Generated by Django 2.0.13 on 2020-04-14 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_auto_20200414_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enroll',
            name='lecture_list',
        ),
        migrations.RemoveField(
            model_name='enroll',
            name='user',
        ),
        migrations.DeleteModel(
            name='enroll',
        ),
    ]
