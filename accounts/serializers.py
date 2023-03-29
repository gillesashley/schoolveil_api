from rest_framework import serializers
from schools.models import School


class SchoolLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('email', 'password')
