from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Exam(models.Model):
    SUBJECT_STATUS = [
        (0, '语文'),
        (1, '英语'),
        (2, '数学'),
    ]

    title = models.CharField(max_length=200)
    subject = models.IntegerField(choices=SUBJECT_STATUS)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='exam')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
