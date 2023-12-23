from django.urls import path
from .views import PostListView


urlpatterns = [
    path('club_news/', PostListView.as_view(), name='club_news')
]