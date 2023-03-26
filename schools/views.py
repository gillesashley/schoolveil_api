from django.shortcuts import get_object_or_404
from rest_framework import viewsets
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
