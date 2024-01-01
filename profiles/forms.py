from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Profile


class EditUserForm(UserChangeForm):
    # Remove the password field
    password = None
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

class EditProfileForm(forms.ModelForm):

    # set about_me to a textarea widget to stop HTML tags appearing
    about_me = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Profile
        fields = ('profile_pic', 'about_me',)

