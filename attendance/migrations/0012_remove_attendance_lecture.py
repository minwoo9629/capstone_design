# Generated by Django 2.0.13 on 2020-04-18 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0011_auto_20200418_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='lecture',
        ),
    ]