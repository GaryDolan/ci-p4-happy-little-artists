from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Profile
from .forms import EditProfileForm, EditUserForm
class ProfileDetailView(generic.DetailView):
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
        return get_object_or_404(Profile, user=user) # self.object is now the user profile of given username

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Set the flag (highlights profile tab in nav) but only if its your profile
        context['current_page'] = 'profile' if self.request.user == self.object.user else None

        # Paginate the users blog like by 3
        liked_post_paginator = Paginator(self.object.user.blog_likes.all(), 3)
        page = self.request.GET.get('page')
        liked_posts = liked_post_paginator.get_page(page)
        context['liked_posts'] = liked_posts


        return context

class EditProfileView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Profile
    template_name = 'edit_profile.html'
    form_class = EditProfileForm
    # user_form_class = EditUserForm

    # Override the get success to redirect back to the specific user profile page 
    def get_success_url(self):
        return reverse_lazy('profile', args=[self.object.user.username])
    # 
    def test_func(self):
        return self.request.user == self.get_object().user