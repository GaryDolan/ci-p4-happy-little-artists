from django import forms
from django.core.validators import RegexValidator
from .models import Booking, ArtClass

class BookingForm(forms.ModelForm):

    #define regex validators
    # Only letters and spaces
    name_validator = RegexValidator(regex=r'^[a-zA-Z\s]+$', message='Only letters and spaces are allowed.', code='invalid_name')

    # Only numbers in the format xxx xxx xxxx
    phone_num_validator = RegexValidator(regex=r'^(\d{3}\s?\d{3}\s?\d{4}|\(\d{3}\)\d{3}\d{4})$', message='Enter a phone number in the format xxx xxx xxxx.',code='invalid_phone_number')

    child_name = forms.CharField(max_length=20, validators=[name_validator], help_text="Enter name (letters only)")
    contact_number = forms.CharField(max_length=20, validators=[phone_num_validator], help_text="Enter number in the format XXX XXX XXXX")
    emg_contact_name = forms.CharField(max_length=20, validators=[name_validator], help_text="Enter name (letters only)")
    emg_contact_number = forms.CharField(max_length=20, validators=[phone_num_validator], help_text="Enter number in the format XXX XXX XXXX")
    class Meta:
        model = Booking
        fields = ('art_class', 'child_name', 'contact_number', 'emg_contact_name', 'emg_contact_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set the values of the are class field to all available art classes
        self.fields['art_class'].queryset=ArtClass.objects.all()