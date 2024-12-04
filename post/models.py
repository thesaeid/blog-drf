from django.contrib.auth import get_user_model
from django.utils.text import Truncator
from django.db import models


user_model = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(user_model, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField(Tag, related_name="blog_posts", blank=True)

    def __str__(self):
        return Truncator(self.title).chars(15)


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(user_model, on_delete=models.CASCADE)
    post = models.ForeignKey(
        BlogPost,
        related_name="comments",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return Truncator(self.content).chars(15)
