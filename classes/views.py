from rest_framework import viewsets
from rest_framework.exceptions import NotFound

from classes.models import Class
from classes.serializers import ClassSerializer


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    lookup_field = 'slug'

    def get_object(self):
        queryset = self.get_queryset()
        slug = self.kwargs.get('slug')
        obj = queryset.filter(slug=slug).first()
        if obj is None:
            raise NotFound('Class not found')
        return obj
