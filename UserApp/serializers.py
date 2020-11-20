from rest_framework import serializers
from .models import UserApp


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserApp
        fields = ('username', 'password', 'first_name', 'last_name', 'is_active',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserApp(
            username=validated_data['username']

        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class GetUserAppSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserApp
        fields = ('id', 'username', 'first_name', 'last_name', 'is_active', 'last_login', 'is_superuser')
        # fields = '__all__'

