# Generated by Django 2.0.13 on 2020-04-14 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0018_professor_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professor',
            old_name='major_code',
            new_name='major',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='bye',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='hi',
        ),
    ]
