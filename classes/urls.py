from django.urls import path, include
from rest_framework.routers import DefaultRouter
from classes.views import ClassViewSet

router = DefaultRouter()
router.register(r'classes', ClassViewSet, basename='class')

urlpatterns = [
    path('', include(router.urls)),
    path('gradings/', include('gradings.urls')),
    path('students/', include('students.urls')),
    path('subjects/', include('subjects.urls')),
]
