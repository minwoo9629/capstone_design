# Generated by Django 2.0.13 on 2020-04-13 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0009_auto_20200413_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='hi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hi', models.CharField(max_length=30)),
            ],
        ),
    ]