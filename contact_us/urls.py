"""URL patterns for the contact_us app"""
from django.urls import path
from .views import ContactUsView


urlpatterns = [
    path('contact_us/', ContactUsView.as_view(), name='contact_us')
]
