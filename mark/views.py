from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

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
    filterset_fields = ['classes']
    permission_classes = [IsAuthenticated]


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
