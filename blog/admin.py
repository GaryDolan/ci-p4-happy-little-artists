from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status', 'author','created_on', 'modified_on')
    list_filter = ('status', 'created_on', 'modified_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    
    actions = ['set_as_draft', 'publish_post', 'archive_post']

    def set_as_draft(self, request, queryset):
        queryset.update(status=0)

    def publish_post(self, request, queryset):
        queryset.update(status=1)

    def archive_post(self, request, queryset):
        queryset.update(status=2)



