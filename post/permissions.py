from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Allows access only to admins.
    """

    def has_permission(self, request, view):
        return request.user and request.user.role == "admin"


class IsAuthor(BasePermission):
    """
    Allows access to authors to modify their own blog posts.
    """

    def has_permission(self, request, view):
        return request.user and request.user.role == "author"

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsReader(BasePermission):
    """
    Allows access to readers for read-only actions.
    """

    def has_permission(self, request, view):
        return request.user and request.user.role in ["reader", "author", "admin"]

    def has_object_permission(self, request, view, obj):
        return view.action in ["retrieve", "list"]


class CanComment(BasePermission):
    """
    Allows readers and authors to comment on blog posts.
    """

    def has_permission(self, request, view):
        return request.user and request.user.role in ["author", "reader", "admin"]
