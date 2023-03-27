from django.urls import path
from .views import TeacherListCreateAPIView, TeacherDetailAPIView

app_name = 'teachers'

urlpatterns = [
    path('', TeacherListCreateAPIView.as_view(), name='teacher-list'),
    path('<int:pk>/', TeacherDetailAPIView.as_view(), name='teacher-detail'),
]
