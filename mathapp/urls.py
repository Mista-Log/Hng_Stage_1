from django.urls import path
from . import views






urlpatterns = [
    path('api/classify-number/', views.MathAPIView.as_view()),
]