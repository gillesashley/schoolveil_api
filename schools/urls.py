from django.urls import path, include
from rest_framework import routers
from schools.views import SchoolViewSet

router = routers.DefaultRouter()
router.register(r'', SchoolViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<slug:slug>/', include(router.urls)),
    path('teachers/', include('teachers.urls')),
    path('subjects/', include('subjects.urls')),
    path('departments/', include('departments.urls')),
    path('years-terms/', include('years_terms.urls')),
    path('classes/', include('classes.urls')),
    path('grading/', include('gradings.urls')),
    path('auth/accounts/', include('accounts.urls'))
]
