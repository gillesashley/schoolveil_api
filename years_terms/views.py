from rest_framework import viewsets, status
from rest_framework.response import Response
from datetime import date
from django.utils import timezone
from years_terms.models import YearsTerms
from schools.models import School
from years_terms.serializers import YearsTermsSerializer


class YearsTermsViewSet(viewsets.ModelViewSet):
    queryset = YearsTerms.objects.all()
    serializer_class = YearsTermsSerializer

    def create(self, request, *args, **kwargs):
        # Deactivate old term
        active_term = YearsTerms.objects.filter(is_active=True).first()
        current_date = timezone.now().date()

        if active_term and current_date >= active_term.end_date:
            active_term.is_active = False
            active_term.save()

        # Create new term
        school = School.objects.get(name="Example School")
        new_term = YearsTerms(
            name="Term 3",
            start_date=date(2023, 5, 1),
            end_date=date(2023, 7, 31),
            school=school,
            is_active=True
        )

        new_term.save()

        serializer = self.get_serializer(new_term)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
