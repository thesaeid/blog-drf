from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from .models import User


class UserCreateSerializer(BaseUserCreateSerializer):
    ROLE_CHOICES = (("author", "Author"), ("reader", "Reader"))
    role = serializers.ChoiceField(choices=ROLE_CHOICES)

    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ("id", "username", "password", "email", "role")

    def validate_role(self, value):
        if value not in ["author", "reader"]:
            raise serializers.ValidationError(
                "You can only choose 'author' or 'reader'."
            )
        return value
