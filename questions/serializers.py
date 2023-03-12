from django.contrib.auth.models import User
from rest_framework import serializers
from questions.models import SingleChoice


class SingleChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SingleChoice
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'is_superuser')

# class QuestionsListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Question
#         fields = [
#             'id',
#             'body',
#             'created',
#         ]
#
#
# class SingleChoicesListSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name='single_choice_detail')
#
#     class Meta:
#         model = SingleChoice
#         fields = [
#             # 'id',
#             'body',
#             'url'
#         ]
#
#
# class SingleChoiceDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SingleChoice
#         fields = '__all__'
