from django.shortcuts import get_object_or_404
from rest_framework import viewsets, serializers, status
from rest_framework.response import Response

from schools.models import School
from schools.serializers import SchoolSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    lookup_field = 'slug'

    def get_object(self):
        queryset = self.get_queryset()
        slug = self.kwargs['slug']
        obj = get_object_or_404(queryset, slug=slug)
        return obj

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')
        if School.objects.filter(email=email).exists():
            return Response({'email': ['This email is already in use.']}, status=status.HTTP_400_BAD_REQUEST)
        elif School.objects.filter(phone_number=phone_number).exists():
            return Response({'phone_number': ['This phone number is already in use.']},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
