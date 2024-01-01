from django.contrib import admin
from .models import ArtClass, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ArtClass)
class ArtClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'duration', 'location', 'age_group', 'bookings_count', 'max_bookings')
    search_fields = ('title', 'location')
    list_filter = ('age_group','location')
    
@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('owner', 'child_name', 'art_class', 'payment_status', 'date_created')
    list_filter = ('owner', 'child_name', 'art_class__title', 'payment_status','date_created')
    search_fields = ['owner__username', 'child_name']
    summernote_fields = ('admin_notes',)
    
    actions = ['mark_as_paid', 'mark_as_not_paid']

    def mark_as_not_paid(self, request, queryset):
        queryset.update(payment_status=0)
        self.message_user(request, f'selected bookings have been marked as not paid.')

    def mark_as_paid(self, request, queryset):
        queryset.update(payment_status=1)
        self.message_user(request, f'selected bookings have been marked as paid.')
