"""
Views for the blog app.
"""
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import CommentForm


class PostListView(generic.ListView):
    """
    A class based view for displaying a list of club news posts.
    """
    model = Post
    # pylint: disable=no-member
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'club_news.html'
    paginate_by = 4
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        """
        Overrides the get_context_data method to add a variable to
        context before its returned
        """
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'club_news'
        return context


class PostDetailView(View):
    """
    A class based view for displaying the details of a single club news post.
    """
    def get(self, request, slug):
        """
        Handles the get request for the posts detailed page.

        Obtains the post object from the list of approved posts and approved
        comments related to this post. Set some vars and renders the page via
        the post_details.html template.
        """
        current_page = 'club_news'
        # pylint: disable=no-member
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
                'commented': False,
                'liked': liked,
                'current_page': current_page,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug):
        """
        Handles the post request for the posts detailed page.

        Obtains the post object from the list of approved posts and approved
        comments related to this post. Set some vars.

        Renders the page via the post_details.html template base on if the
        users comments are valid.
        """
        current_page = 'club_news'
        # pylint: disable=no-member
        published_posts = Post.objects.filter(status=1)
        post = get_object_or_404(published_posts, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Check if user is logged in
        if request.user.is_authenticated:
            # Retrieve form data
            comment_form = CommentForm(data=request.POST)
            # for valid forms update the model fields not filled out
            if comment_form.is_valid():
                comment_form.instance.user = request.user
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
                messages.success(
                    request, 'You have successfully added a comment.')
            else:
                comment_form = CommentForm()
        else:
            messages.error(request, 'You must be logged in to post a comment.')
            return redirect(reverse('account_login'))

        return render(
            request,
            'post_details.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'current_page': current_page,
                'comment_form': comment_form
            },
        )


class PostLikeView(LoginRequiredMixin, View):
    """
    A class based view to handel liking and unliking posts in the
    post detail view.
    """
    login_url = 'account_login'

    def post(self, request, slug):
        """
        Handles the post request for the liking and unliking or posts.

        Obtains the post object and add or removes it from a post based on if
        user has previously liked the post.

        Redirects to the post_details.html template via its url.
        """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.warning(request, 'You have unliked this post.')
        else:
            post.likes.add(request.user)
            messages.success(request, 'You have liked this post.')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
