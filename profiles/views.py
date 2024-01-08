"""
Views for the profiles app.
"""
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views import generic
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from bookings.models import Booking
from .models import Profile
from .forms import EditProfileForm, EditUserForm


class ProfileDetailView(generic.DetailView):
    """
    A class based view for displaying the details of a single profile.
    """
    model = Profile
    template_name = "profile.html"
    # Name to refer to it by in the template
    context_object_name = "profile"

    def get_object(self, queryset=None):

        # Get the username from the URL
        username = self.kwargs.get('username')

        # Find the user object with username in URL
        user = get_object_or_404(User, username=username)

        # Find the profile with username attached
        # self.object is now the user profile of given username
        return get_object_or_404(Profile, user=user)

    def get_context_data(self, **kwargs):
        """
        Handles the get request for the profile page.

        Obtains and returns the users liked posts (with pagination) an
        user bookings.
        """
        context = super().get_context_data(**kwargs)

        # Set the flag (highlights profile tab in nav) only if its your profile
        context['current_page'] = (
            'profile' if self.request.user == self.object.user else None)

        # Paginate the users blog like by 3
        liked_post_paginator = Paginator(self.object.user.blog_likes.all(), 3)
        page = self.request.GET.get('page')
        liked_posts = liked_post_paginator.get_page(page)
        context['liked_posts'] = liked_posts

        # get and return user bookings to the template
        # pylint: disable=no-member
        context['user_bookings'] = (
            Booking.objects.filter(owner=self.object.user))
        return context


class EditProfileView(LoginRequiredMixin,
                      UserPassesTestMixin, generic.UpdateView):
    """
    A class based view to handel profile editing.
    """
    model = Profile
    template_name = 'edit_profile.html'
    form_class = EditProfileForm

    def get_success_url(self):
        """
        Overrides the get success method to redirect to the specific user
        profile page.
        """
        messages.success(
            self.request, 'You have successfully updated your profile.')
        return reverse_lazy('profile', args=[self.object.user.username])

    def test_func(self):
        """
        Test function for UserPassesTestMixin. Passes if user trying to edit
        profile is the profile owner.
        """
        return self.request.user == self.get_object().user


class EditUserView(LoginRequiredMixin,
                   UserPassesTestMixin, generic.UpdateView):
    """
    A class based view to handel user info editing.
    """
    model = User
    template_name = 'edit_user.html'
    form_class = EditUserForm

    def get_success_url(self):
        """
        Overrides the get success method to redirect to the specific user
        profile page.
        """
        messages.success(
            self.request, 'You have successfully updated your user info.')
        return reverse_lazy('profile', args=[self.object.username])

    def test_func(self):
        """
        Test function for UserPassesTestMixin. Passes if user is trying to edit
        their own info
        """
        return self.request.user == self.get_object()
