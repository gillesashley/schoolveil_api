from rest_framework import viewsets
from gradings.models import Grading
from gradings.serializers import GradingSerializer


class GradingViewSet(viewsets.ModelViewSet):
    queryset = Grading.objects.all()
    serializer_class = GradingSerializer

    def get_queryset(self):
        queryset = Grading.objects.filter(student__id=self.kwargs['student_id'])
        return queryset
