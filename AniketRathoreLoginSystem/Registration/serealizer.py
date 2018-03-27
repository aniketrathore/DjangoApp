from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class ShowUserDataSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class RegisterNewUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class UserUpdateViewSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserDeleteView(ModelSerializer):
    class Meta:
        model = User
        fields = ('username')
