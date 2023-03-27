from rest_framework import serializers
from teachers.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class_name = serializers.CharField(source='classroom.class_name', read_only=True)
    class_id = serializers.IntegerField(source='classroom.id', read_only=True)
    school_name = serializers.CharField(source='school.name', read_only=True)
    school_id = serializers.IntegerField(source='school.id', read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'classroom', 'class_name',
                  'class_id', 'school', 'school_name', 'school_id']
