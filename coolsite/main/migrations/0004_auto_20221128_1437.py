# Generated by Django 3.2.16 on 2022-11-28 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20221128_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='student',
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.group')),
            ],
        ),
    ]
