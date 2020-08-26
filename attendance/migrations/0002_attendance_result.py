# Generated by Django 2.0.13 on 2020-03-18 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='result',
            field=models.CharField(choices=[('ATTEND', '출석'), ('LATE', '지각'), ('ABSENT', '결석')], default=True, max_length=10),
        ),
    ]