# Generated by Django 2.0.13 on 2020-03-25 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_postattend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postattend',
            name='user',
        ),
        migrations.DeleteModel(
            name='PostAttend',
        ),
    ]
