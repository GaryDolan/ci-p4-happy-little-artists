from django.urls import path
from .views import ProfileDetailView, EditProfileView


urlpatterns = [
    path('<str:username>/', ProfileDetailView.as_view(), name='profile'),
    path('edit_profile/<slug:pk>/', EditProfileView.as_view(), name='edit_profile'),
]