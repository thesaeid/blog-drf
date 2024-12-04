from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


from .models import Tag, BlogPost
from .serializers import BlogPostSerializer, BlogPostCreateSerializer, TagSerializer
from .filters import BlogPostFilter
from .paginations import BlogPostPagination

user_model = get_user_model()


class BlogPostAPI(APIView):
    def get(self, request):
        posts = BlogPost.objects.all().prefetch_related("tags").order_by("-created_at")

        blog_filter = BlogPostFilter(request.GET, queryset=posts)

        paginator = BlogPostPagination()
        result_page = paginator.paginate_queryset(blog_filter.qs, request)

        serializer = BlogPostSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        try:
            user = user_model.objects.get(username=request.user)
            if user.role in ["author", "admin"]:
                serializer = BlogPostCreateSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                title = serializer.data["title"]
                content = serializer.data["content"]
                tags = serializer.data["tags"]
                author = user

                post = BlogPost.objects.create(
                    title=title,
                    content=content,
                    author=author,
                )

                tag_instances = []
                for tag_name in tags:
                    tag, created = Tag.objects.get_or_create(name=tag_name["name"])
                    tag_instances.append(tag)

                post.tags.set(tag_instances)
                post.save()
                return Response(
                    data="Your Post is Published.",
                    status=status.HTTP_201_CREATED,
                )

            return Response(
                data="You're not allowed to make a post.",
                status=status.HTTP_403_FORBIDDEN,
            )
        except user_model.DoesNotExist:
            return Response(
                data="You're not allowed to do this.",
                status=status.HTTP_403_FORBIDDEN,
            )

    def put(self, request, id):
        try:
            user = user_model.objects.get(username=request.user)
            post = get_object_or_404(BlogPost, pk=id)

            if user.role == "admin" or post.author == user:
                serializer = BlogPostCreateSerializer(post, data=request.data)
                if serializer.is_valid():
                    post.title = serializer.validated_data["title"]
                    post.content = serializer.validated_data["content"]
                    post.save()

                    # Update tags if provided
                    tags = serializer.validated_data.get("tags", [])
                    if tags:
                        tag_instances = []
                        for tag_name in tags:
                            tag, created = Tag.objects.get_or_create(
                                name=tag_name["name"]
                            )
                            tag_instances.append(tag)

                        post.tags.set(tag_instances)
                        post.save()

                    return Response(
                        data={
                            "message": "Post updated successfully.",
                            "post": BlogPostSerializer(post).data,
                        },
                        status=status.HTTP_200_OK,
                    )

                return Response(
                    data=serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return Response(
                data={"message": "You're not allowed to update this post."},
                status=status.HTTP_403_FORBIDDEN,
            )
        except user_model.DoesNotExist:
            return Response(
                data="You're not allowed to do this.",
                status=status.HTTP_403_FORBIDDEN,
            )

    def delete(self, request, id):
        try:
            user = user_model.objects.get(username=request.user)
            if user.role == "admin":
                post = get_object_or_404(BlogPost, pk=id)
                post.delete()

                return Response(
                    data={"message": "Post deleted successfully."},
                    status=status.HTTP_204_NO_CONTENT,
                )
            elif user.role == "author":
                post = get_object_or_404(BlogPost, pk=id)
                if post.author == user:
                    post.delete()
                    return Response(
                        data={"message": "Post deleted successfully."},
                        status=status.HTTP_204_NO_CONTENT,
                    )
                return Response(
                    data={"message": "You're not allowed to delete this post."},
                    status=status.HTTP_403_FORBIDDEN,
                )

            return Response(
                data={"message": "You're not allowed to delete a post."},
                status=status.HTTP_403_FORBIDDEN,
            )
        except user_model.DoesNotExist:
            return Response(
                data="You're not allowed to do this.",
                status=status.HTTP_403_FORBIDDEN,
            )
