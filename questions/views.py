from django.shortcuts import render
from django.http import HttpResponse
from questions.models import Question
from questions.serializers import QuestionsListSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def index(request):
    return HttpResponse("questions view")


@api_view(['GET', 'POST'])
def questions_list(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionsListSerializer(questions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuestionsListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
