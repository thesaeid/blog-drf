import django_filters

from .models import BlogPost


class BlogPostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    content = django_filters.CharFilter(field_name="content", lookup_expr="icontains")
    tags = django_filters.CharFilter(
        field_name="tags__name", lookup_expr="icontains"
    )  # Filter by tag name
    author = django_filters.CharFilter(
        field_name="author__username", lookup_expr="icontains"
    )  # Filter by author's username
    start_date = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="gte"
    )  # Filter posts from a specific date
    end_date = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="lte"
    )  # Filter posts until a specific date

    class Meta:
        model = BlogPost
        fields = ["title", "content", "tags", "author", "start_date", "end_date"]
