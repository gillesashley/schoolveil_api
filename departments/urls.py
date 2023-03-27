from django.urls import path, include
from rest_framework import routers
from .views import DepartmentViewSet

router = routers.DefaultRouter()
router.register(r'', DepartmentViewSet, basename='department')

app_name = 'departments'
urlpatterns = [
    path('', include(router.urls)),
]
