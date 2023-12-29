from django.contrib import admin
from django.utils.text import slugify
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status', 'author','created_on', 'modified_on')
    list_filter = ('status', 'created_on', 'modified_on', 'author__username')
    search_fields = ['author__username', 'title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    
    actions = ['set_as_draft', 'publish_post', 'archive_post']

    def set_as_draft(self, request, queryset):
        queryset.update(status=0)
        self.message_user(request, f'selected posts have been set as drafts.')

    def publish_post(self, request, queryset):
        queryset.update(status=1)
        self.message_user(request, f'selected posts have been published.')

    def archive_post(self, request, queryset):
        queryset.update(status=2)
        self.message_user(request, f'selected posts have been archived.')
    
    # Override the save model to update slug when posts is edited 
    def save_model(self, request, obj, form, change):
        if change and 'title' in form.changed_data:
            obj.slug = slugify(obj.title)

        super().save_model(request, obj, form, change)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment_text', 'post', 'created_on','approved')
    list_filter = ('approved', 'created_on', 'user__username')
    search_fields = ['user__username', 'comment_text']
    actions = ['approve_comments', 'disapprove_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, f'selected comments have been approved.')
    
    def disapprove_comments(self, request, queryset):
        queryset.update(approved=False)
        self.message_user(request, f'selected comments have been disapproved.')
