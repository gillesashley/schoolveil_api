from rest_framework import viewsets

from teachers.models import Teacher
from teachers.serializers import TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'slug'

    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        obj = queryset.get(slug=self.kwargs[self.lookup_field])
        self.check_object_permissions(self.request, obj)
        return obj
