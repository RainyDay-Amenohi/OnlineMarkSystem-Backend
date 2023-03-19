from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

# 单选题的数据模型
# class SingleChoice(models.Model):
#     body = models.TextField()
#     choices_1 = models.CharField(max_length=200)
#     choices_2 = models.CharField(max_length=200)
#     choices_3 = models.CharField(max_length=200)
#     choices_4 = models.CharField(max_length=200)
#     right_answer = models.CharField(max_length=1)
#     author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#
#     def __str__(self):
#         return self.body
#
#     class Meta:
#         ordering = ['-id']


# 选择题数据模型
class ChoiceQuestion(models.Model):
    class SubjectStatus(models.IntegerChoices):
        CHI = 0, '语文',
        ENG = 1, '英语',
        MAT = 2, '数学',

    class TypeStatus(models.IntegerChoices):
        SINGLE = 0, '单项选择',
        MULTIPLE = 1, '多项选择'

    body = models.TextField()
    choices_A = models.CharField(max_length=200)
    choices_B = models.CharField(max_length=200)
    choices_C = models.CharField(max_length=200)
    choices_D = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=10)
    image = models.ImageField(upload_to='img', blank=True, null=True)
    subject = models.IntegerField(choices=SubjectStatus.choices, null=True)
    type = models.IntegerField(choices=TypeStatus.choices)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['-id']


# 主观题数据模型
class SubjectiveQuestion(models.Model):
    class SubjectStatus(models.IntegerChoices):
        CHI = 0, '语文',
        ENG = 1, '英语',
        MAT = 2, '数学',

    body = models.TextField()
    correct_answer = models.TextField()
    image = models.ImageField(upload_to='img', blank=True, null=True)
    subject = models.IntegerField(choices=SubjectStatus.choices, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['-id']
