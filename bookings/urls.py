from django.urls import path
from .views import CreateBookingView, EditBookingView


urlpatterns = [
    path('create_booking/', CreateBookingView.as_view(), name='create_booking'),
    path('edit_user/<int:pk>/', EditBookingView.as_view(), name='edit_booking'),
]