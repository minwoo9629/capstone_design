# Generated by Django 3.0.3 on 2020-03-10 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0003_auto_20200310_1831'),
        ('lecture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='prof_code',
            field=models.ForeignKey(db_column='prof_code', on_delete=django.db.models.deletion.CASCADE, to='professor.Professor', to_field='prof_code'),
        ),
    ]
