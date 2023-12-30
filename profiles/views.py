from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Profile

class ProfileDetailView(generic.DetailView):
    model = Profile 
    template_name = "profile.html"
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

        #Get users liked posts
        context['liked_posts'] = self.object.user.blog_likes.all()


        return context

