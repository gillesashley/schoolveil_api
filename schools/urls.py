from django.urls import path, include
from rest_framework import routers
from schools.views import SchoolViewSet

router = routers.DefaultRouter()
router.register(r'schools', SchoolViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('schools/<slug:slug>/', include(router.urls)),
    path('teachers', include('teachers.urls')),
    path('departments', include('departments.urls')),
]
