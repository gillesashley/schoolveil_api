from rest_framework import serializers
from gradings.models import Grading
from students.serializers import StudentSerializer
from subjects.serializers import SubjectSerializer


class GradingSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = Grading
        fields = ['id', 'student', 'subject', 'school', 'score', 'out_of', 'date']
