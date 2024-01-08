"""
Django app configuration for the authentication app.
"""
from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """
    AppConfig for the authentication app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'
