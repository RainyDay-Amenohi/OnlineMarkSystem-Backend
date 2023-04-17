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
    score = serializers.IntegerField(required=False, default=0)
    # 在反序列化的时候，接收一个主键值或者一个包含多个主键值的列表，然后根据queryset参数找到对应的模型对象
    exam = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all())

    class Meta:
        model = ExamQuestion
        fields = '__all__'
