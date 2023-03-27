from rest_framework import serializers
from .models import YearsTerms


class YearsTermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearsTerms
        fields = '__all__'
