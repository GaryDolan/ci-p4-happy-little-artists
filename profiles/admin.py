from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    list_display = ('user', 'about_me', 'created_on')
    list_filter=('created_on', 'user__is_active')
    search_fields = ['user__username', 'about_me']
    summernote_fields = ('about_me',)
