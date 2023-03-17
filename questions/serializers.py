from django.contrib.auth.models import User
from rest_framework import serializers
from questions.models import SingleChoice, ChoiceQuestion


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'is_superuser')


class SingleChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SingleChoice
        fields = '__all__'


class ChoiceQuestionSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = ChoiceQuestion
        fields = '__all__'
