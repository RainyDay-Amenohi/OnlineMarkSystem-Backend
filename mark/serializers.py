from rest_framework import serializers

from exams.serializers import ExamSerializer
from mark.models import Class, ClassExam, Answer, Student
from questions.models import ChoiceQuestion, BlankQuestion, SubjectiveQuestion
from questions.serializers import BlankQuestionSerializer, ChoiceQuestionSerializer


class ClassSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='class-detail')

    class Meta:
        model = Class
        fields = '__all__'


class ClassExamSerializer(serializers.ModelSerializer):
    classes = ClassSerializer(read_only=True)
    exam = ExamSerializer(read_only=True)

    class Meta:
        model = ClassExam
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='student-detail')

    class Meta:
        model = Student
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='answer-detail')
    correct = serializers.SerializerMethodField()
    question_body = serializers.SerializerMethodField()

    # score = serializers.SerializerMethodField()

    def get_correct(self, obj):
        if obj.question_type == 0 or obj.question_type == 1:
            correct = ChoiceQuestion.objects.get(id=obj.question_id).correct_answer
            if correct == obj.context:
                obj.score = 1
            else:
                obj.score = 0
            return correct
        elif obj.question_type == 2:
            blank = BlankQuestion.objects.get(id=obj.question_id)
            if blank.blanks_num == 1:
                return str(blank.correct_answer_1)
            elif blank.blanks_num == 2:
                return str(blank.correct_answer_1) + ';' + str(blank.correct_answer_2)
            else:
                return str(blank.correct_answer_1) + ';' + str(blank.correct_answer_2) + ';' + str(
                    blank.correct_answer_3)
        else:
            return SubjectiveQuestion.objects.get(id=obj.question_id).correct_answer

    def get_question_body(self, obj):
        if obj.question_type == 0 or obj.question_type == 1:
            return ChoiceQuestion.objects.get(id=obj.question_id).body
        elif obj.question_type == 2:
            blank = BlankQuestion.objects.get(id=obj.question_id)
            return BlankQuestion.objects.get(id=obj.question_id).body
        else:
            return SubjectiveQuestion.objects.get(id=obj.question_id).body

    class Meta:
        model = Answer
        fields = '__all__'
