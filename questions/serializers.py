from rest_framework import serializers
from questions.models import Question


class QuestionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'body',
            'created',
        ]
