from django.shortcuts import render
from django.views import generic
from blog.models import Post

class IndexView(generic.View):
    
    def get(self, request):
        recent_posts = Post.objects.filter(status=1).order_by('-created_on')[:3]
        return render(request, 'index.html',{'recent_posts': recent_posts})
