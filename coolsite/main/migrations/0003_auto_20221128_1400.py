# Generated by Django 3.2.16 on 2022-11-28 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_group_lesson_rename_status_requeststatus_student_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='lesson',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.lesson'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='number',
            field=models.IntegerField(),
        ),
    ]
