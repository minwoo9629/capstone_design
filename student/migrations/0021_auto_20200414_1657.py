# Generated by Django 2.0.13 on 2020-04-14 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0012_remove_lecture_prof_code'),
        ('student', '0020_delete_enroll'),
    ]

    operations = [
        migrations.CreateModel(
            name='TakeLectures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lectures', models.ForeignKey(db_column='lectures', on_delete=django.db.models.deletion.CASCADE, to='lecture.Lecture', to_field='code', verbose_name='수강 강의')),
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to='student.Student', to_field='username', verbose_name='학번')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='take_lectures',
            field=models.ManyToManyField(through='student.TakeLectures', to='lecture.Lecture', verbose_name='수강 강의'),
        ),
    ]