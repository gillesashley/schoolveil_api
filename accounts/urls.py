from django.urls import path
from accounts.views import SchoolLoginView

urlpatterns = [
    path('login/', SchoolLoginView.as_view(), name="school-login"),
]
