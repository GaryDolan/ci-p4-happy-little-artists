from django.urls import path
from .views import ProfileDetailView, EditProfileView, EditUserView


urlpatterns = [
    path('<str:username>/', ProfileDetailView.as_view(), name='profile'),
    path('edit_profile/<slug:pk>/', EditProfileView.as_view(), name='edit_profile'),
    path('edit_user/<slug:pk>/', EditUserView.as_view(), name='edit_user'),
]