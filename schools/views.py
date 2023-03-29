from django.shortcuts import get_object_or_404
from rest_framework import viewsets, serializers
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
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        except serializers.ValidationError as e:
            return Response(e.detail, status=400)
