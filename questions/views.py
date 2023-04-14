from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from questions.models import ChoiceQuestion, SubjectiveQuestion, BlankQuestion
from questions.serializers import ChoiceQuestionSerializer, \
    SubjectiveQuestionSerializer, BlankQuestionSerializer
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.views import APIView
from questions.permission import IsAdminUserOrReadOnly


# Create your views here.
def index(request):
    return HttpResponse("questions view")


class ChoiceQuestionViewSet(viewsets.ModelViewSet):
    queryset = ChoiceQuestion.objects.all()
    serializer_class = ChoiceQuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'type']
    permission_classes = [IsAdminUserOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(methods=['get'], detail=False, url_path='random')
    def get_random(self, request):
        # self 参数是指 MyViewSet 实例本身，而 request 参数是指 HTTP 请求对象
        single_num = int(request.query_params['singleNum'])
        multiple_num = int(request.query_params['multipleNum'])
        subject = int(request.query_params['subject'])

        # 过滤科目并获取随机题目
        queryset_1 = ChoiceQuestion.objects.filter(subject=subject, type=0).order_by('?')[
                     :single_num]
        queryset_2 = ChoiceQuestion.objects.filter(subject=subject, type=1).order_by('?')[:multiple_num]
        serializer_1 = ChoiceQuestionSerializer(queryset_1, context={'request': request}, many=True)
        serializer_2 = ChoiceQuestionSerializer(queryset_2, context={'request': request}, many=True)

        # python推导式,返回type url id
        id_list = [{'question_id': obj['id'], 'type': obj['type'], 'question_url': obj['url']} for obj in
                   serializer_1.data] + \
                  [{'question_id': obj['id'], 'type': obj['type'], 'question_url': obj['url']} for obj in
                   serializer_2.data]
        return Response(id_list)


class BlankQuestionViewSet(viewsets.ModelViewSet):
    queryset = BlankQuestion.objects.all()
    serializer_class = BlankQuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'subject']
    permission_classes = [IsAdminUserOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(methods=['get'], detail=False, url_path='random')
    def get_random(self, request):
        num = int(request.query_params['num'])
        subject = int(request.query_params['subject'])

        queryset = BlankQuestion.objects.filter(subject=subject).order_by('?')[:num]
        serializer = BlankQuestionSerializer(queryset, context={'request': request}, many=True)

        # python推导式,返回type url id
        id_list = [{'question_id': obj['id'], 'type': 2, 'question_url': obj['url']} for obj in serializer.data]
        return Response(id_list)


class SubjectiveQuestionViewSet(viewsets.ModelViewSet):
    queryset = SubjectiveQuestion.objects.all()
    serializer_class = SubjectiveQuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'subject']
    permission_classes = [IsAdminUserOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(methods=['get'], detail=False, url_path='random')
    def get_random(self, request):
        num = int(request.query_params['num'])
        subject = int(request.query_params['subject'])

        queryset = SubjectiveQuestion.objects.filter(subject=subject).order_by('?')[:num]
        serializer = SubjectiveQuestionSerializer(queryset, context={'request': request}, many=True)

        # python推导式,返回type url id
        id_list = [{'question_id': obj['id'], 'type': 3, 'question_url': obj['url']} for obj in serializer.data]
        return Response(id_list)
