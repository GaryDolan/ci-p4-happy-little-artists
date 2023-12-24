from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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

class PostDetailView(View):

    def get (self, request, slug, *args, **kwargs):
        current_page = 'club_news'
        published_posts = Post.objects.filter(status=1)
        post = get_object_or_404(published_posts, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'post_details.html',
            {
                'post': post,
                'comments': comments,
                'liked': liked,
                'current_page': current_page
            },
        )
