from django.urls import path
from . import views






urlpatterns = [
    path('/api/classify-number/<int:n>/', views.MathAPIView.as_view()),
]