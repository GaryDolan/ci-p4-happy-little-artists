from django import forms
from .models import Booking, ArtClass

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('art_class', 'child_name', 'contact_number', 'emg_contact_name', 'emg_contact_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set the values of the are class field to all available art classes 
        self.fields['art_class'].queryset=ArtClass.objects.all()