"""
Forms for handling bookings in the bookings app.
"""
from django import forms
from django.core.validators import RegexValidator
from django.db.models import F, Q
from django.utils.safestring import mark_safe
from .models import Booking, ArtClass


class BookingForm(forms.ModelForm):
    """
    Form for handling creation of bookings.
    """
    # define regex validators
    # Only letters and spaces
    name_validator = RegexValidator(
        regex=r'^[a-zA-Z\s]+$',
        message='Only letters and spaces are allowed.',
        code='invalid_name')

    # Only numbers in the format xxx xxx xxxx
    phone_num_validator = RegexValidator(
        regex=r'^(\d{3}\s?\d{3}\s?\d{4}|\(\d{3}\)\d{3}\d{4})$',
        message='Enter a phone number in the format xxx xxx xxxx.',
        code='invalid_phone_number')

    child_name = forms.CharField(
        max_length=20,
        validators=[name_validator],
        help_text="Enter name (letters only)")
    contact_number = forms.CharField(
        max_length=20,
        validators=[phone_num_validator],
        help_text="Enter number in the format XXX XXX XXXX")
    emg_contact_name = forms.CharField(
        max_length=20,
        validators=[name_validator],
        help_text="Enter name (letters only)")
    emg_contact_number = forms.CharField(
        max_length=20,
        validators=[phone_num_validator],
        help_text="Enter number in the format XXX XXX XXXX")

    class Meta:
        """
        Uses booking model for the form and includes art_class, child_name,
        contact_number, emg_contact_name and emg_contact_number.
        """
        model = Booking
        fields = ('art_class', 'child_name', 'contact_number',
                  'emg_contact_name', 'emg_contact_number')

    def __init__(self, *args, **kwargs):
        """
        Override the initialise method of the form so that the art class
        dropdown can be created dynamically based on available class spaces.
        """
        super().__init__(*args, **kwargs)

        # set the values of the art class field to a dropdown(queryset)
        # of all art classes that are not full
        # F allows comparison of 2 model fields in filters
        # pylint: disable=no-member
        self.fields['art_class'].queryset = ArtClass.objects.filter(
            bookings_count__lt=F("max_bookings"))

        # if there are entries in the query
        if not self.fields['art_class'].queryset.exists():
            # use the widget to modify the art class fields disabled attribute
            self.fields['art_class'].widget.attrs.update({'disabled': True})
            self.fields['art_class'].help_text = mark_safe(
                    '<span class="classes-full">All classes are full. '
                    'Please try again later.</span>')
            self.fields['art_class'].label = mark_safe(
                '<span class="classes-full">Art Class (All full).</span>')


class EditBookingForm(forms.ModelForm):
    """
    Form for handling editing of bookings.
    """
    # define regex validators
    # Only letters and spaces
    name_validator = RegexValidator(
        regex=r'^[a-zA-Z\s]+$',
        message='Only letters and spaces are allowed.',
        code='invalid_name')

    # Only numbers in the format xxx xxx xxxx
    phone_num_validator = RegexValidator(
        regex=r'^(\d{3}\s?\d{3}\s?\d{4}|\(\d{3}\)\d{3}\d{4})$',
        message='Enter a phone number in the format xxx xxx xxxx.',
        code='invalid_phone_number')

    # Set up form fields
    child_name = forms.CharField(
        max_length=20,
        validators=[name_validator],
        help_text="Enter name (letters only)")
    contact_number = forms.CharField(
        max_length=20,
        validators=[phone_num_validator],
        help_text="Enter number in the format XXX XXX XXXX")
    emg_contact_name = forms.CharField(
        max_length=20,
        validators=[name_validator],
        help_text="Enter name (letters only)")
    emg_contact_number = forms.CharField(
        max_length=20,
        validators=[phone_num_validator],
        help_text="Enter number in the format XXX XXX XXXX")

    class Meta:
        """
        Use booking model for the form and include art_class, child_name,
        contact_number, emg_contact_name and emg_contact_number.
        """
        model = Booking
        fields = ('art_class', 'child_name', 'contact_number',
                  'emg_contact_name', 'emg_contact_number')

    def __init__(self, *args, **kwargs):
        """
        Override the initialise method of the form so that the art class
        dropdown can be will include the art class associated with the booking
        regardless of if that art club is full.
        """
        super().__init__(*args, **kwargs)

        # get the art class attached to the booking being modified by this form
        # art class id passed to view, then to form when view creates form
        current_art_class = self.instance.art_class

        # set the values of the art class field to a dropdown(queryset)of all
        # art classes that are not full and the current art class
        # F allows comparison of 2 model fields in filters
        # Q allows queries with multiple conditions
        # pylint: disable=no-member
        self.fields['art_class'].queryset = ArtClass.objects.filter(
                Q(bookings_count__lt=F("max_bookings")) |
                Q(pk=current_art_class.pk))
