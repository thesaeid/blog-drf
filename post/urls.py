from django.urls import path

from .apis import BlogPostAPI, CommentAPI

urlpatterns = [
    path(
        "posts/",
        BlogPostAPI.as_view(),
        name="blogpost-list",
    ),
    path(
        "posts/<int:id>/",
        BlogPostAPI.as_view(),
        name="blogpost-delete",
    ),
    path(
        "posts/<int:post_id>/comments/",
        CommentAPI.as_view(),
        name="comment-list",
    ),
    path(
        "posts/<int:post_id>/comments/<int:comment_id>/",
        CommentAPI.as_view(),
        name="comment-delete",
    ),
]
