from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from exams.models import Exam, ExamQuestion
from exams.serializer import ExamSerializer, ExamQuestionSerializer


# Create your views here.
class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ExamQuestionViewSet(viewsets.ModelViewSet):
    queryset = ExamQuestion.objects.all()
    serializer_class = ExamQuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['exam']
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
