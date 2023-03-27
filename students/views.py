from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import filters
from students.models import Student
from students.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'email', 'phone_number']

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        slug = self.kwargs['slug']
        first_name, last_name = slug.split('-')
        obj = get_object_or_404(queryset, first_name=first_name, last_name=last_name)
        self.check_object_permissions(self.request, obj)
        return obj
