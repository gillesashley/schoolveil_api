from rest_framework import serializers
from subjects.models import Subject
from teachers.serializers import TeacherSerializer


class SubjectSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()

    class Meta:
        model = Subject
        fields = ['id', 'name', 'slug', 'description', 'teacher', 'start_time', 'end_time']
        read_only_fields = ['id', 'slug']
