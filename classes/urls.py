from rest_framework import routers
from classes.views import ClassViewSet

router = routers.DefaultRouter()
router.register(r'', ClassViewSet, basename='class')

urlpatterns = router.urls
