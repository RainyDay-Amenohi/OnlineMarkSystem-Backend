import json

from django.core import serializers
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from exams.models import ExamQuestion, Exam
from mark.models import Class, ClassExam, Answer, Student
from mark.serializers import ClassSerializer, ClassExamSerializer, AnswerSerializer, StudentSerializer


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['name']
    permission_classes = [IsAuthenticated]


class ClassExamViewSet(viewsets.ModelViewSet):
    queryset = ClassExam.objects.all()
    serializer_class = ClassExamSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['classes', 'exam']
    permission_classes = [IsAuthenticated]

    # 计算班级成绩分布
    @action(methods=['get'], detail=True, url_path='class-grade')
    def class_grade(self, request, pk):
        grade_list = [{'name': '60以下', 'value': 0}, {'name': '60-70', 'value': 0}, {'name': '70-80', 'value': 0},
                      {'name': '80-90', 'value': 0}, {'name': '90以上', 'value': 0}]
        class_id = self.queryset.get(pk=pk).classes_id
        exam_id = self.queryset.get(pk=pk).exam_id
        # 获取所有学生
        students = Student.objects.filter(classes_id=class_id)
        exam_name = Exam.objects.get(id=exam_id).title

        # 每一个学生的得分
        for stu in students:
            for item in stu.scores:
                if item['title'] == exam_name:
                    s = item['score']
                    if s < 60:
                        grade_list[0]['value'] += 1
                    elif s < 70:
                        grade_list[1]['value'] += 1
                    elif s < 80:
                        grade_list[2]['value'] += 1
                    elif s < 90:
                        grade_list[3]['value'] += 1
                    else:
                        grade_list[4]['value'] += 1
        json_list = json.dumps(grade_list)
        return Response(json_list)

    # 计算得分率
    @action(methods=['get'], detail=True, url_path='score-rate')
    def score_rate(self, request, pk):
        class_id = self.queryset.get(pk=pk).classes_id
        exam_id = self.queryset.get(pk=pk).exam_id
        print(exam_id)
        # 获取所有学生
        students = Student.objects.filter(classes_id=class_id)
        # 获取每一题的得分率
        # 先拿到单题的分值，用每一个答案的得分除以分值得出得分率，最后将所有得分率求平均
        questions = ExamQuestion.objects.filter(exam=exam_id)
        general_rate = []
        for q in questions:
            # rates数组保存一道题目中每一个学生的得分率
            rates = []
            for stu in students:
                grade = Answer.objects.get(student=stu.id, question_id=q.question_id).score
                rate = grade / q.score
                print(grade)
                print(q.score)
                rates.append(rate)
            # 求出一道题的平均得分率
            avg_rate = (sum(rates) / len(rates)) * 100
            general_rate.append(avg_rate)
        # print(general_rate)
        json_list = json.dumps(general_rate)
        return Response(json_list)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['question_id', 'question_type', 'student', 'exam']
    permission_classes = [IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['classes']
    permission_classes = [IsAuthenticated]
