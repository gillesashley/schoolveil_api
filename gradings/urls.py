from django.urls import path, include
from rest_framework import routers
from gradings.views import GradingViewSet

router = routers.DefaultRouter()
router.register(r'gradings', GradingViewSet)

app_name = 'gradings'
urlpatterns = [
    path('', include(router.urls)),
]
