# Generated by Django 2.0.13 on 2020-05-12 08:48

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0004_auto_20200322_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='name',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='학부(학과) 이름'),
        ),
        migrations.AlterField(
            model_name='college',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='university.College', verbose_name='학부 선택'),
        ),
    ]