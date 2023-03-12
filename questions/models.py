from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


# 单选题的数据模型
class SingleChoice(models.Model):
    body = models.TextField()
    choices_1 = models.CharField(max_length=200)
    choices_2 = models.CharField(max_length=200)
    choices_3 = models.CharField(max_length=200)
    choices_4 = models.CharField(max_length=200)
    right_answer = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['-id']

