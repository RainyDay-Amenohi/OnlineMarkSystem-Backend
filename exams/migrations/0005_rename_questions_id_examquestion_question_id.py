# Generated by Django 4.1.7 on 2023-04-06 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_examquestion_questions_id_alter_examquestion_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examquestion',
            old_name='questions_id',
            new_name='question_id',
        ),
    ]
