# Generated by Django 4.1.7 on 2023-03-19 04:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0012_remove_subjectivequestion_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectivequestion',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subjectivequestion',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='subjectivequestion',
            name='subject',
            field=models.IntegerField(choices=[(0, '语文'), (1, '英语'), (2, '数学')], null=True),
        ),
    ]
