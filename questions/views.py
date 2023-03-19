from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django_filters.rest_framework import DjangoFilterBackend

from questions.models import ChoiceQuestion, SubjectiveQuestion
from questions.serializers import UserSerializer, ChoiceQuestionSerializer, \
    SubjectiveQuestionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.views import APIView


# Create your views here.
def index(request):
    return HttpResponse("questions view")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class SingleChoiceViewSet(viewsets.ModelViewSet):
#     queryset = SingleChoice.objects.all()
#     serializer_class = SingleChoiceSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['author', 'body']
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)


class ChoiceQuestionViewSet(viewsets.ModelViewSet):
    queryset = ChoiceQuestion.objects.all()
    serializer_class = ChoiceQuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'type']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class SubjectiveQuestionViewSet(viewsets.ModelViewSet):
    queryset = SubjectiveQuestion.objects.all()
    serializer_class = SubjectiveQuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'subject']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
