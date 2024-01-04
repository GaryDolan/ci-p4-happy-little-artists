from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import	HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import CommentForm


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on') # pylint: disable=no-member
    template_name = 'club_news.html'
    paginate_by = 4
    context_object_name = 'posts'

    # override get_context_data method to add a variable to context before its returned
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'club_news'
        return context

class PostDetailView(View):

    def get (self, request, slug):
        current_page = 'club_news'
        published_posts = Post.objects.filter(status=1) # pylint: disable=no-member
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

    def post (self, request, slug):
        current_page = 'club_news'
        published_posts = Post.objects.filter(status=1) # pylint: disable=no-member
        post = get_object_or_404(published_posts, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Check if user is logged in
        if request.user.is_authenticated:
            # Retrieve form data
            comment_form = CommentForm(data=request.POST)
            # for valid forms update the model fields not filled out in the form
            if comment_form.is_valid():
                comment_form.instance.user = request.user
                comment = comment_form.save(commit=False)
                comment.post =post
                comment.save()
                messages.success(request, 'You have successfully added a comment.')
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
    login_url = 'account_login'

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.warning(request, 'You have unliked this post.')
        else:
            post.likes.add(request.user)
            messages.success(request, 'You have liked this post.')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
