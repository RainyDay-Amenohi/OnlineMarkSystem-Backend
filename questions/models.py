from django.db import models
from django.utils import timezone


# Create your models here.

# 问题的数据模型
class Question(models.Model):
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.body
