from rest_framework.routers import DefaultRouter
from subjects.views import SubjectViewSet

router = DefaultRouter()
router.register(r'', SubjectViewSet, basename='subject')

urlpatterns = router.urls
