from rest_framework import serializers
from .models import UserApp


class GetUserAppSerializer(serializers.ModelSerializer):
    """вывод пользователя"""
    class Meta:
        model = UserApp
        exclude = (
            "email",
            "is_staff",
            "date_joined"
        )


class GetUserListSerializer(serializers.ModelSerializer):
    """ список пользователей """
    class Meta:
        model = UserApp
        fields = ('id', 'username')

