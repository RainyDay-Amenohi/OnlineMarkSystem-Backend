# Generated by Django 4.1.7 on 2023-04-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('mark', '0007_alter_student_scores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='scores',
            field=models.JSONField(default=list),
        ),
    ]
