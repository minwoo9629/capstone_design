# Generated by Django 2.0.13 on 2020-03-18 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0003_auto_20200318_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='code',
            new_name='lecture_code',
        ),
        migrations.RemoveField(
            model_name='room',
            name='name',
        ),
    ]
