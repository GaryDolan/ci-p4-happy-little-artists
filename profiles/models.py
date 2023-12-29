from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    profile_pic = ResizedImageField(quality=100, upload_to="p4/profile_images/", force_format='WEBP')
    about_me = models.TextField(help_text='Enter your about me info here', blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    # not a newly created profile
    instance.profile.save()
