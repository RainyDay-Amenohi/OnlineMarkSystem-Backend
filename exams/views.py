from django.http import FileResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from exams.models import Exam, ExamQuestion
from questions.models import ChoiceQuestion, BlankQuestion, SubjectiveQuestion
from exams.serializers import ExamSerializer, ExamQuestionSerializer

from exams import pdf


# Create your views here.
class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(methods=['get'], detail=True, url_path='exam-pdf')
    def exam_pdf(self, request, pk):
        # 获取题目信息
        exam = Exam.objects.get(pk=pk)
        question_infos = ExamQuestion.objects.filter(exam=exam)
        singles = []
        multiples = []
        blanks = []
        subjectives = []
        for item in question_infos:
            if item.type == 0:
                singles.append(ChoiceQuestion.objects.get(pk=item.question_id))
            elif item.type == 1:
                multiples.append(ChoiceQuestion.objects.get(pk=item.question_id))
            elif item.type == 2:
                blanks.append(BlankQuestion.objects.get(pk=item.question_id))
            else:
                subjectives.append(SubjectiveQuestion.objects.get(pk=item.question_id))
        url = self.request.build_absolute_uri('/') + pdf.print_exam(exam, singles, multiples, blanks, subjectives)
        return Response(url)


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
