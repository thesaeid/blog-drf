from django.urls import path

from .apis import BlogPostAPI

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
]
