"""
URL patterns for the about_us app
"""
from django.urls import path
from .views import AboutUsView

urlpatterns = [
    path('about_us/', AboutUsView.as_view(), name='about_us')
]
