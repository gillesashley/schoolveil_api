from rest_framework import serializers
from students.models import Student
from classes.serializers import ClassSerializer


class StudentSerializer(serializers.ModelSerializer):
    class_name = ClassSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'email', 'phone_number', 'street_address',
                  'guardian', 'class_name']
