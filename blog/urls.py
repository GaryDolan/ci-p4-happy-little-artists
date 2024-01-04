from django.urls import path
from .views import PostListView, PostDetailView, PostLikeView


urlpatterns = [
    path('club_news/', PostListView.as_view(), name='club_news'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('like/<slug:slug>/', PostLikeView.as_view(), name='post_like'),
]
