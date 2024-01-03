from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import Booking
from .forms import BookingForm

class CreateBookingView(LoginRequiredMixin, generic.CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'create_booking.html'
    # Return to current users profile
    
    # Override the form valid (save) method to assign the booking owner 
    def form_valid(self, form):
        messages.success(self.request, 'You have successfully created a booking.')
        form.instance.owner =self.request.user
        return super().form_valid(form)
    
    #override the get success_url method to dynamically call the correct user profile
    def get_success_url(self):
        return reverse('profile', kwargs={'username': self.request.user.username})
    
class EditBookingView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Booking
    template_name = 'edit_booking.html'
    form_class = BookingForm

    # Override the get success to redirect back to the specific user profile page 
    def get_success_url(self):
        messages.success(self.request, 'You have successfully updated your booking.')
        return reverse_lazy('profile', args=[self.object.owner.username])
    
    # Test function for UserPassesTestMixin
    def test_func(self):
        return self.request.user == self.get_object().owner
    
