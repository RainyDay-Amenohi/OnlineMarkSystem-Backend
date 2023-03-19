from django.contrib.auth.models import User
from rest_framework import serializers
from questions.models import ChoiceQuestion, SubjectiveQuestion


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'is_superuser')


# class SingleChoiceSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = SingleChoice
#         fields = '__all__'


class ChoiceQuestionSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)
    subject_name = serializers.ReadOnlyField(source='get_subject_display')
    type_name = serializers.ReadOnlyField(source='get_type_display')

    class Meta:
        model = ChoiceQuestion
        fields = '__all__'


class SubjectiveQuestionSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    subject_name = serializers.ReadOnlyField(source='get_subject_display')

    class Meta:
        model = SubjectiveQuestion
        fields = '__all__'
