from django.urls import path, include
from rest_framework import routers
from teachers.views import TeacherViewSet

router = routers.DefaultRouter()
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('teachers/<slug:slug>/', include(router.urls)),
]
