from rest_framework import serializers
from exams.models import Exam, ExamQuestion
from user_info.serializer import UserDescSerializer


class ExamSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='exam-detail')
    author = UserDescSerializer(read_only=True)
    subject_name = serializers.ReadOnlyField(source='get_subject_display')
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M', required=False)
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M', required=False)

    class Meta:
        model = Exam
        fields = '__all__'


class ExamQuestionSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='examquestion-detail')
    type_name = serializers.ReadOnlyField(source='get_type_display')
    exam = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all())

    class Meta:
        model = ExamQuestion
        fields = '__all__'
