from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'years-terms', views.YearsTermsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
