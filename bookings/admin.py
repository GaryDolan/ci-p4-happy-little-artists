from django.contrib import admin
from .models import ArtClass
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ArtClass)
class ArtClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'duration', 'location', 'age_group', 'bookings_count', 'max_bookings')
    search_fields = ('title', 'location')
    list_filter = ('age_group','location')
    
