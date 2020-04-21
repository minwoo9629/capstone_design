# Generated by Django 2.0.13 on 2020-04-18 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0022_auto_20200418_1418'),
        ('attendance', '0012_remove_attendance_lecture'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='lecture',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='lecture.Lecture'),
            preserve_default=False,
        ),
    ]
