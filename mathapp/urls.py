from django.urls import path
from . import views






urlpatterns = [
    path('number_properties/<int:number>/', views.MathAPIView.as_view()),
]