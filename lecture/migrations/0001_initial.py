# Generated by Django 3.0.7 on 2020-08-03 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('professor', '0001_initial'),
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='강의실 코드')),
                ('building', models.CharField(max_length=20, verbose_name='동')),
                ('number', models.CharField(max_length=20, verbose_name='호수')),
            ],
        ),

         migrations.CreateModel(
            name='GiveLectures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username',models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to='professor.Professor', to_field='username', verbose_name='교수')),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='강의명')),
                ('code', models.CharField(max_length=20, verbose_name='강의 코드')),
                ('split_code', models.CharField(max_length=3, unique=True, verbose_name='분반 코드')),
                ('semester', models.CharField(choices=[('1st_semester', '1'), ('Seconde_semester', '2')], max_length=20, verbose_name='학기')),
                ('day_of_the_week', models.CharField(max_length=10, null=True, verbose_name='수업 요일')),
                ('start_time', models.TimeField(default='00:00', verbose_name='수업 시작 시간')),
                ('end_time', models.TimeField(default='00:00', verbose_name='수업 종료 시간')),
                ('term', models.CharField(choices=[('15', '15'), ('30', '30'), ('45', '45'), ('60', '60')], default='30', max_length=5, verbose_name='출석 반복 시간')),
                ('count', models.IntegerField(null=True, verbose_name='반복 횟수')),
                ('professor', models.ManyToManyField(through='lecture.GiveLectures', to='professor.Professor', verbose_name='교수')),
                ('room_code', models.ForeignKey(db_column='room_code', on_delete=django.db.models.deletion.CASCADE, to='lecture.Room', to_field='code')),
            ],
        ),
       migrations.AddField(
            model_name='GiveLectures',
            name='lectures',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lecture.Lecture', verbose_name='담당 강의'),
        ),
        
        
        migrations.CreateModel(
            name='Beacon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=10, verbose_name='비콘 major 값')),
                ('minor', models.CharField(max_length=10, verbose_name='비콘 minor 값')),
                ('room_code', models.OneToOneField(db_column='room_code', on_delete=django.db.models.deletion.CASCADE, to='lecture.Room', to_field='code', verbose_name='강의실 코드')),
                ('uuid', models.ForeignKey(db_column='uuid', limit_choices_to={'level': 0}, max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='university.College', to_field='uuid', verbose_name='학교와 대응되는 비콘 UUID 값')),
            ],
        ),
    ]
