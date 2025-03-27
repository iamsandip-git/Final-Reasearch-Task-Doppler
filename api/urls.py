from django.urls import path
from .views import ListNews
from .views import health_check

urlpatterns = [
    path("", ListNews.as_view()),
    path('health', health_check, name='health-check'),
]
