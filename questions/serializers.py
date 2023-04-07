from django.contrib.auth.models import User
from rest_framework import serializers
from questions.models import ChoiceQuestion, SubjectiveQuestion, BlankQuestion
from user_info.serializer import UserDescSerializer


class ChoiceQuestionSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDescSerializer(read_only=True)
    subject_name = serializers.ReadOnlyField(source='get_subject_display')
    type_name = serializers.ReadOnlyField(source='get_type_display')
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ChoiceQuestion
        fields = '__all__'


class BlankQuestionSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDescSerializer(read_only=True)
    subject_name = serializers.ReadOnlyField(source='get_subject_display')
    type_name = serializers.CharField(default='填空题')
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BlankQuestion
        fields = '__all__'


class SubjectiveQuestionSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDescSerializer(read_only=True)
    subject_name = serializers.ReadOnlyField(source='get_subject_display')
    type_name = serializers.CharField(default='主观题')
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SubjectiveQuestion
        fields = '__all__'
