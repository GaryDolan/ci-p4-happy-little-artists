"""
Class based models for blog app
"""
from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

# Tuple to control posts status
STATUS = ((0, "Draft"), (1, "Published"), (2, "Archived"))


class Post(models.Model):
    """
    Model to represent a blog post
    """
    title = models.CharField(
        max_length=100, unique=True, help_text='Enter a post title')
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    description = models.CharField(
        max_length=200, help_text='Enter a brief post description')
    featured_img = ResizedImageField(
        quality=75, upload_to="p4/post_images/", force_format='WEBP')
    additional_img1 = ResizedImageField(
        quality=75,
        upload_to="p4/post_images/",
        force_format='WEBP',
        blank=True)
    additional_img2 = ResizedImageField(
        quality=75,
        upload_to="p4/post_images/",
        force_format='WEBP',
        blank=True)
    additional_img3 = ResizedImageField(
        quality=75,
        upload_to="p4/post_images/",
        force_format='WEBP',
        blank=True)
    additional_img4 = ResizedImageField(
        quality=75,
        upload_to="p4/post_images/",
        force_format='WEBP',
        blank=True)
    additional_img5 = ResizedImageField(
        quality=75,
        upload_to="p4/post_images/",
        force_format='WEBP',
        blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    content = models.TextField(help_text='Enter the post text here')
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """
        Defines the display ordering (descending) of the post model
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string based on the posts title
        """
        # pylint: disable=invalid-str-returned
        return self.title

    def number_of_likes(self):
        """
        Return the number of like a particular post has
        """
        # pylint: disable=no-member
        return self.likes.count()

    def number_of_comments(self):
        """
        Return the number of comments a particular post has
        """
        # pylint: disable=no-member
        return self.comments.filter(approved=True).count()


class Comment(models.Model):

    """
    Model to represent a comment on a blog post
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField(help_text='Enter your comment here')
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Defines the display ordering (ascending) of the post model
        """
        ordering = ['created_on']

    def __str__(self):
        """
        Returns a string based on the comment and the user that posted it
        """
        return f"Comment {self.comment_text} by {self.user}"
