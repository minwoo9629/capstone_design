# Generated by Django 2.0.13 on 2020-04-13 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0009_auto_20200413_1719'),
        ('student', '0010_auto_20200413_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enroll',
            name='lecture_list',
        ),
        migrations.AddField(
            model_name='enroll',
            name='lecture',
            field=models.ForeignKey(db_column='lecture', default='L001', on_delete=django.db.models.deletion.CASCADE, to='lecture.Lecture', to_field='code', verbose_name='수강 강의'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='lecture_list',
            field=models.ManyToManyField(through='student.enroll', to='lecture.Lecture', verbose_name='수강 강의'),
        ),
        migrations.AlterField(
            model_name='enroll',
            name='username',
            field=models.ForeignKey(db_column='username', default='test', on_delete=django.db.models.deletion.CASCADE, to='student.Student', to_field='username', verbose_name='학번'),
        ),
    ]
