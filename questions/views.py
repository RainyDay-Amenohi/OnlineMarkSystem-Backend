from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django_filters.rest_framework import DjangoFilterBackend

from questions.models import SingleChoice
from questions.serializers import SingleChoiceSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.views import APIView


# Create your views here.
def index(request):
    return HttpResponse("questions view")


class SingleChoiceViewSet(viewsets.ModelViewSet):
    queryset = SingleChoice.objects.all()
    serializer_class = SingleChoiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'body']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# @api_view(['GET', 'POST'])
# def questions_list(request):
#     if request.method == 'GET':
#         questions = Question.objects.all()
#         serializer = QuestionsListSerializer(questions, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = QuestionsListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def single_choices_list(request):
#     if request.method == 'GET':
#         single_choices = SingleChoice.objects.all()
#         serializer = SingleChoicesListSerializer(single_choices, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = SingleChoicesListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class SingleChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = SingleChoice.objects.all()
#     serializer_class = SingleChoiceDetailSerializer

# class SingleChoiceDetail(APIView):
#     # 获取单个题目对象
#     def get_object(self, pk):
#         try:
#             return SingleChoice.objects.get(pk=pk)
#         except:
#             raise Http404
#
#     def get(self, request, pk):
#         single_choice = self.get_object(pk)
#         serializer = SingleChoiceDetailSerializer(single_choice)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         single_choice = self.get_object(pk)
#         serializer = SingleChoiceDetailSerializer(single_choice, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         single_choice = self.get_object(pk)
#         single_choice.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
