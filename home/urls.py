"""URL patterns for the home app"""
from django.urls import path
from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='home')
]
