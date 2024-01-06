from django import forms
from django.core.validators import RegexValidator
from django.db.models import F, Q
from django.utils.safestring import mark_safe
from .models import Booking, ArtClass

# Use the same form for booking and editing booking
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

        # set the values of the art class field to a dropdown(queryset)of all art classes that are not full
        # F allows comparison of 2 model fields in filters
        self.fields['art_class'].queryset = ArtClass.objects.filter(bookings_count__lt=F("max_bookings")) # pylint: disable=no-member

        # if there are entries in the query
        if not self.fields['art_class'].queryset.exists():
            # use the widget to modify the art class fields disabled attribute
            self.fields['art_class'].widget.attrs.update ({'disabled': True})
            self.fields['art_class'].help_text = mark_safe('<span class="classes-full">All classes are full. Please try again later.</span>')
            self.fields['art_class'].label = mark_safe('<span class="classes-full">Art Class (All full).</span>')


class EditBookingForm(forms.ModelForm):
    #define regex validators
    # Only letters and spaces
    name_validator = RegexValidator(regex=r'^[a-zA-Z\s]+$', message='Only letters and spaces are allowed.', code='invalid_name')

    # Only numbers in the format xxx xxx xxxx
    phone_num_validator = RegexValidator(regex=r'^(\d{3}\s?\d{3}\s?\d{4}|\(\d{3}\)\d{3}\d{4})$', message='Enter a phone number in the format xxx xxx xxxx.',code='invalid_phone_number')

    # Set up form fields
    child_name = forms.CharField(max_length=20, validators=[name_validator], help_text="Enter name (letters only)")
    contact_number = forms.CharField(max_length=20, validators=[phone_num_validator], help_text="Enter number in the format XXX XXX XXXX")
    emg_contact_name = forms.CharField(max_length=20, validators=[name_validator], help_text="Enter name (letters only)")
    emg_contact_number = forms.CharField(max_length=20, validators=[phone_num_validator], help_text="Enter number in the format XXX XXX XXXX")
    class Meta:
        model = Booking
        fields = ('art_class', 'child_name', 'contact_number', 'emg_contact_name', 'emg_contact_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # get the art class attached to the booking being modified by this form
        # id was passed to view and when view creates form he booking info is passed
        current_art_class = self.instance.art_class

        # set the values of the art class field to a dropdown(queryset)of all art classes that are not full and the current art class
        # F allows comparison of 2 model fields in filters
        # Q allows queries with multiple conditions

        self.fields['art_class'].queryset = ArtClass.objects.filter(Q(bookings_count__lt=F("max_bookings")) | Q(pk=current_art_class.pk)) # pylint: disable=no-member
