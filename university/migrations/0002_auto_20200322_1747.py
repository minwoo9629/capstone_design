# Generated by Django 2.0.13 on 2020-03-22 08:47

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='category',
        ),
        migrations.AddField(
            model_name='department',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, db_column='parent', null=True, on_delete=django.db.models.deletion.CASCADE, to='university.College', verbose_name='대학 이름'),
        ),
        migrations.AlterField(
            model_name='college',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='university.College'),
        ),
    ]