# Generated by Django 2.0.13 on 2020-04-14 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0011_delete_hi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='prof_code',
        ),
    ]