from rest_framework import serializers
from exams.models import Exam
from user_info.serializer import UserDescSerializer


class ExamSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='exam-detail')
    author = UserDescSerializer(read_only=True)
    subject_name = serializers.ReadOnlyField(source='get_subject_display')

    class Meta:
        model = Exam
        fields = '__all__'
