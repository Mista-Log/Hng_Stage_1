from django.urls import path
from . import views






urlpatterns = [
    path('number_properties/<int:n>/', views.MathAPIView.as_view()),
]