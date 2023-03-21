from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from questions.models import ChoiceQuestion, SubjectiveQuestion, BlankQuestion
from questions.serializers import ChoiceQuestionSerializer, \
    SubjectiveQuestionSerializer, BlankQuestionSerializer
from rest_framework.decorators import api_view
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


class BlankQuestionViewSet(viewsets.ModelViewSet):
    queryset = BlankQuestion.objects.all()
    serializer_class = BlankQuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'subject']
    permission_classes = [IsAdminUserOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class SubjectiveQuestionViewSet(viewsets.ModelViewSet):
    queryset = SubjectiveQuestion.objects.all()
    serializer_class = SubjectiveQuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'subject']
    permission_classes = [IsAdminUserOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
