"""
Views for the home app.
"""
from django.shortcuts import render
from django.views import View
from blog.models import Post


class IndexView(View):
    """
    A class based view for displaying the home page.
    """
    def get(self, request):
        """
        Renders the home page, providing a list of the most recent four club
        news posts.
        """
        # pylint: disable=no-member
        recent_posts = (Post.objects.filter(status=1)
                        .order_by('-created_on')[:4])
        current_page = 'home'
        return render(request,
                      'index.html',
                      {'recent_posts': recent_posts,
                       'current_page': current_page})
