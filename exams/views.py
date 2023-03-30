from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from exams.models import Exam
from exams.serializer import ExamSerializer


# Create your views here.
class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
