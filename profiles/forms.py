"""
Forms for handling editing profile and user info in the profiles app.
"""
from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Profile


class EditUserForm(UserChangeForm):
    """
    Form to handle editing user info.
    """
    # Remove the password field
    password = None

    # define regex validators

    # Only letters and spaces
    name_validator = RegexValidator(
        regex=r'^[a-zA-Z\s]+$',
        message='Only letters and spaces are allowed.',
        code='invalid_name')

    first_name = forms.CharField(
        max_length=20,
        validators=[name_validator],
        help_text="Enter name (letters only)")

    last_name = forms.CharField(
        max_length=20,
        validators=[name_validator],
        help_text="Enter name (letters only)")

    email = forms.EmailField(
        max_length=254,
        help_text="Enter email address")

    class Meta:
        """
        Uses profile model for the form and includes first_name,
        last_name and email.
        """
        model = User
        fields = ('first_name', 'last_name', 'email',)


class EditProfileForm(forms.ModelForm):
    """
    Form to handle editing profile info.
    """
    # set about_me to a textarea widget to stop HTML tags appearing
    about_me = forms.CharField(widget=forms.Textarea)

    class Meta:
        """
        Uses profile model for the form and includes profile_pic and about_me.
        """
        model = Profile
        fields = ('profile_pic', 'about_me',)
