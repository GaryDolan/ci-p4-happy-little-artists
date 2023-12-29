from django.urls import path
from .views import PostListView, PostDetailView, PostLike


urlpatterns = [
    path('club_news/', PostListView.as_view(), name='club_news'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('like/<slug:slug>/', PostLike.as_view(), name='post_like'),
]