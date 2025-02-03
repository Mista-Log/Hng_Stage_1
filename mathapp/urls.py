from django.urls import path
from . import views






urlpatterns = [
    path('api/classify-number/<str:n>/', views.MathAPIView.as_view()),
]