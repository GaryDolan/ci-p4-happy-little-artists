from django.urls import path
from .views import CreateBookingView, EditBookingView, DeleteBookingView


urlpatterns = [
    path('create_booking/', CreateBookingView.as_view(), name='create_booking'),
    path('edit_booking/<int:pk>/', EditBookingView.as_view(), name='edit_booking'),
    path('delete_booking/', DeleteBookingView.as_view(), name='delete_booking'),
]
