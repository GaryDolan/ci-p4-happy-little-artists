"""
Class based models for profiles app
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_resized import ResizedImageField


class Profile(models.Model):
    """
    Model to represent a user profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    profile_pic = ResizedImageField(
        quality=100,
        upload_to="p4/profile_images/",
        force_format='WEBP')
    about_me = models.TextField(
        help_text='Enter your about me info here',
        blank=True)

    def __str__(self):
        """
        Returns a string based on the profiles users username
        """
        # pylint: disable=no-member
        return self.user.username


@receiver(post_save, sender=User)
# pylint: disable=unused-argument
def create_or_update_profile(instance, created, **kwargs):
    """
    uses the post_save signal of the user model to create a user
    profile related to the user, when a user is created
    """
    if created:
        # pylint: disable=no-member
        Profile.objects.create(user=instance)
    # not a newly created profile
    instance.profile.save()
