from rest_framework import routers

from teachers.views import TeacherViewSet

router = routers.DefaultRouter()
router.register(r'', TeacherViewSet, basename='teacher')

urlpatterns = router.urls
