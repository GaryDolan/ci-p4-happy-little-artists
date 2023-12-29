from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Profile

class ProfileDetailView(generic.DetailView):
    model = Profile 
    template_name = "profile.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        return get_object_or_404(Profile, user__username=username)

