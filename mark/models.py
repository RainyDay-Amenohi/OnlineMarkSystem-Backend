from django.db import models

# Create your models here.
from exams.models import Exam


class Class(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200)
    student_id = models.IntegerField()
    classes = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.classes.name + '-' + self.name


class ClassExam(models.Model):
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return self.classes.name + '-' + self.exam.title

    class Meta:
        db_table = 'mark_class_exam'


class Answer(models.Model):
    TYPE_STATUS = [
        (0, '单项选择'),
        (1, '多项选择'),
        (2, '填空题'),
        (3, '主观题'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question_type = models.IntegerField(choices=TYPE_STATUS)
    question_id = models.IntegerField()
    context = models.TextField()
    score = models.IntegerField()

    def __str__(self):
        return self.context
