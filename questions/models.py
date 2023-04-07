from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


# 选择题数据模型
class ChoiceQuestion(models.Model):
    SUBJECT_STATUS = [
        (0, '语文'),
        (1, '英语'),
        (2, '数学'),
        (3, '政治'),
    ]

    TYPE_STATUS = [
        (0, '单项选择'),
        (1, '多项选择'),
    ]

    body = models.TextField()
    choices_A = models.CharField(max_length=200)
    choices_B = models.CharField(max_length=200)
    choices_C = models.CharField(max_length=200)
    choices_D = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=10)
    image = models.ImageField(upload_to='img', blank=True, null=True)
    subject = models.IntegerField(choices=SUBJECT_STATUS, null=True)
    type = models.IntegerField(choices=TYPE_STATUS)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='choice')

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['-id']


# 填空题数据模型
class BlankQuestion(models.Model):
    SUBJECT_STATUS = [
        (0, '语文'),
        (1, '英语'),
        (2, '数学'),
        (3, '政治'),
    ]
    body = models.TextField()
    blanks_num = models.IntegerField(default=1)
    correct_answer_1 = models.CharField(max_length=20)
    correct_answer_2 = models.CharField(max_length=20, null=True)
    correct_answer_3 = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='img', blank=True, null=True)
    subject = models.IntegerField(choices=SUBJECT_STATUS, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='blank')

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['-id']


SUBJECT_STATUS = [
    (0, '语文'),
    (1, '英语'),
    (2, '数学'),
    (3, '政治'),
]


# 主观题数据模型
class SubjectiveQuestion(models.Model):
    body = models.TextField()
    correct_answer = models.TextField()
    image = models.ImageField(upload_to='img', blank=True, null=True)
    subject = models.IntegerField(choices=SUBJECT_STATUS, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='subjective')

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['-id']
