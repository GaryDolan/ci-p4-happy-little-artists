"""
Forms for contact_us app.
"""
from django import forms
from django.core.validators import RegexValidator


class ContactUsForm(forms.Form):
    """
    Form for handling user enquiries.
    """
    # define regex validators
    # Only letters and spaces
    name_validator = RegexValidator(
        regex=r'^[a-zA-Z\s]+$',
        message='Only letters and spaces are allowed.',
        code='invalid_name')

    # Only email
    email_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        message='Enter a valid email address.',
        code='invalid_email')
    name = forms.CharField(
        max_length=20,
        validators=[name_validator],
        help_text="Enter name (letters only)")
    email = forms.EmailField(
        max_length=254,
        validators=[email_validator],
        help_text="Enter email address")
    message = forms.CharField(
        widget=forms.Textarea,
        help_text="Enter your message here")
