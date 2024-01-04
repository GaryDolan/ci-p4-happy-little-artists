from django.shortcuts import render
from django.views import View
from blog.models import Post

class IndexView(View):

    def get(self, request):
        recent_posts = Post.objects.filter(status=1).order_by('-created_on')[:4] # pylint: disable=no-member
        current_page = 'home'
        return render(request, 'index.html',{'recent_posts': recent_posts, 'current_page': current_page})
