from rest_framework import serializers

from classes.models import Class
from departments.serializers import DepartmentSerializer
from schools.serializers import SchoolSerializer


class ClassSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    school = SchoolSerializer(read_only=True)

    class Meta:
        model = Class
        fields = ['id', 'name', 'department', 'school', 'teacher', ]

    @staticmethod
    def get_teacher_name(obj):
        return f"{obj.teacher.first_name} {obj.teacher.last_name}"
