# Generated by Django 2.0.13 on 2020-04-14 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0014_auto_20200414_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='major_code',
        ),
    ]