# Generated by Django 5.1.1 on 2024-11-11 01:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0002_alter_course_id_alter_enrollment_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('desc', models.TextField()),
                ('file', models.FileField(upload_to='')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
            options={
                'db_table': 'lecture',
            },
        ),
    ]
