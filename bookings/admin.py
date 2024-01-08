"""
Admin configurations for the booking app
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ArtClass, Booking


@admin.register(ArtClass)
class ArtClassAdmin(admin.ModelAdmin):
    """
    Customises the django admin interface for the art class model
    """
    list_display = (
        'title', 'start_date', 'end_date', 'start_time', 'duration',
        'location', 'age_group', 'bookings_count', 'max_bookings')
    search_fields = ('title', 'location')
    list_filter = ('age_group', 'location', 'age_group')


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    """
    Customises the django admin interface for the booking model
    """
    list_display = ('owner', 'child_name', 'art_class',
                    'payment_status', 'date_created')
    list_filter = ('owner', 'child_name', 'art_class__title',
                   'payment_status', 'date_created')
    search_fields = ['owner__username', 'child_name']
    summernote_fields = ('admin_notes',)

    actions = ['mark_as_paid', 'mark_as_not_paid']

    def mark_as_not_paid(self, request, queryset):
        """
        Allows admin to set a booking as not paid from the admin interface
        """
        queryset.update(payment_status=0)
        self.message_user(request,
                          'selected bookings have been marked as not paid.')

    def mark_as_paid(self, request, queryset):
        """
        Allows admin to set a booking as paid from the admin interface
        """
        queryset.update(payment_status=1)
        self.message_user(request,
                          'selected bookings have been marked as paid.')
