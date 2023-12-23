from django.shortcuts import render
from django.views import generic
from .models import Post

class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'club_news.html'
    paginate_by = 4
    context_object_name = 'posts'

    # override get_context_data method to add a variable to context before its returned
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'club_news'
        return context

    
