# Generated by Django 5.1.1 on 2024-11-11 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0004_alter_quiz_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='desc',
            new_name='description',
        ),
    ]
