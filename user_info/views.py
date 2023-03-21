from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from user_info.serializer import UserDescSerializer


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDescSerializer