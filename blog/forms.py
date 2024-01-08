"""
Forms for handling comments in the blog app.
"""
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form to display comment input.
    """
    class Meta:
        """
        Use comment model for the form and include comment text field.
        """
        model = Comment
        fields = ('comment_text',)
