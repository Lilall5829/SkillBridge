# Generated by Django 5.1.1 on 2024-11-11 18:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0005_rename_desc_quiz_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='desc',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='choices',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='quizzes.questions'),
        ),
    ]
