from django.contrib import admin
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import ArtClass, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ArtClass)
class ArtClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'duration', 'location', 'age_group', 'bookings_count', 'max_bookings')
    search_fields = ('title', 'location')
    list_filter = ('age_group','location', 'age_group')
    
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
    
    # override the save model so that we can update the art class booking count when we add a booking in the admin class
    def save_model(self, request, obj, form, change):
        print('hello')
        # save the booking
        obj.save()
        # update art class count
        obj.art_class.bookings_count = Booking.objects.filter(art_class=obj.art_class).count()
        obj.art_class.save()

# Use the post_delete signal from the booking model to set the booking count of the associated art class
@receiver(post_delete, sender=Booking)
def post_delete_booking(sender, instance, **kwargs):
    art_class = instance.art_class
    remaining_bookings_count = Booking.objects.filter(art_class=art_class).count()
    art_class.bookings_count = remaining_bookings_count
    # only save the booking count
    art_class.save(update_fields=['bookings_count'])