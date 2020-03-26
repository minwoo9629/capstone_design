# Generated by Django 2.0.13 on 2020-03-25 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0002_attendance_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostAttend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beacon_major', models.CharField(max_length=30)),
                ('beacon_minor', models.CharField(max_length=30)),
                ('user', models.ForeignKey(db_column='user', limit_choices_to={'groups__name': 'student'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
