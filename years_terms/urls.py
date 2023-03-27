from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'', views.YearsTermsViewSet, basename='year-term')

app_name = 'years_terms'

urlpatterns = router.urls
