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
    desc = models.CharField(max_length=200)
    subject = models.IntegerField(choices=SUBJECT_STATUS)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='exam')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']


class ExamQuestion(models.Model):
    TYPE_STATUS = [
        (0, '单项选择'),
        (1, '多项选择'),
        (2, '填空题'),
        (3, '主观题'),
    ]

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    type = models.IntegerField(choices=TYPE_STATUS)
    question_url = models.CharField(max_length=200)

    def __str__(self):
        return self.exam.title + '-' + self.question_url

    class Meta:
        db_table = 'exam_question'
