"""
Forms for handling editing profile and user info in the profiles app.
"""
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Profile


class EditUserForm(UserChangeForm):
    """
    Form to handle editing user info.
    """
    # Remove the password field
    password = None

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
